from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.request import Request, urlopen
from urllib.parse import urlparse, parse_qs
from urllib.error import HTTPError
import json, os, time

ROOT=os.path.dirname(os.path.abspath(__file__))
CACHE={}
class Handler(SimpleHTTPRequestHandler):
    def __init__(self,*args,**kwargs): super().__init__(*args,directory=ROOT,**kwargs)
    def do_GET(self):
        p=urlparse(self.path)
        if p.path!='/api/aircraft': return super().do_GET()
        try:
            q=parse_qs(p.query)
            lat=float(q.get('lat',['51.5074'])[0]); lon=float(q.get('lon',['-0.1278'])[0]); radius=max(1,min(100,float(q.get('radius',['25'])[0])))
            if not -90<=lat<=90 or not -180<=lon<=180: raise ValueError('Invalid coordinates')
            key=(round(lat,3),round(lon,3),round(radius,1))
            if key in CACHE and time.time()-CACHE[key][0]<30: data=CACHE[key][1]
            else:
                # OpenSky anonymous quota is limited; one request per 30 seconds per location.
                import math
                dlat=radius/111.0; dlon=radius/max(10,111*math.cos(math.radians(lat)))
                url=f'https://opensky-network.org/api/states/all?lamin={max(-90,lat-dlat):.5f}&lamax={min(90,lat+dlat):.5f}&lomin={max(-180,lon-dlon):.5f}&lomax={min(180,lon+dlon):.5f}'
                req=Request(url,headers={'User-Agent':'SkyAboveMe/1.0 (personal flight viewer)','Accept':'application/json'})
                with urlopen(req,timeout=15) as resp: data=json.load(resp)
                CACHE[key]=(time.time(),data)
            payload=json.dumps({'time':data.get('time'),'states':data.get('states') or []}).encode()
            self.send_response(200)
        except HTTPError as e:
            payload=json.dumps({'error':('OpenSky rate limit reached. Try again later.' if e.code==429 else f'OpenSky returned HTTP {e.code}.')}).encode(); self.send_response(503)
        except Exception as e:
            payload=json.dumps({'error':f'Could not retrieve live aircraft: {str(e)}'}).encode(); self.send_response(503)
        self.send_header('Content-Type','application/json'); self.send_header('Cache-Control','no-store'); self.send_header('Content-Length',str(len(payload))); self.end_headers(); self.wfile.write(payload)
if __name__=='__main__':
    print('Sky Above Me: http://localhost:8000')
    ThreadingHTTPServer(('127.0.0.1',8000),Handler).serve_forever()
