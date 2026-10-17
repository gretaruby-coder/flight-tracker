# Sky Above Me

A full-screen, one-aircraft-at-a-time home flight display inspired by desktop flight information screens.

## Run

1. Install Python 3 if needed.
2. In this folder run `python3 server.py` (macOS/Linux) or `py server.py` (Windows).
3. Visit http://localhost:8000.
4. Click **Use my location** (or enter latitude and longitude), then **Save & start tracking**.

The app refreshes every 30 seconds and shows the closest airborne aircraft inside your chosen radius. When an aircraft leaves, the display changes to the next closest one. A small hysteresis margin avoids rapid switching between similarly close planes.

## Data and limitations

- Aircraft positions are retrieved through a local Python proxy using the OpenSky Network anonymous API. Anonymous usage is rate limited and may be unavailable at times. No API key is required for the default configuration.
- Callsign, altitude, speed, heading, and distance are available when the data provider reports them.
- Airline is *inferred* from the three-letter callsign prefix; this is not guaranteed to be accurate.
- Origin/destination, aircraft model, and aircraft photos are **not** provided by this free API. The live screen displays a dash for unknown routes and a generic stylized plane illustration. Demo mode shows example SFO–LHR data and is clearly labeled.
- Distances are horizontal ground distances, not slant ranges. Closest aircraft does not necessarily mean directly overhead.
- Location is stored in your browser's localStorage, and coordinates are sent to the data provider to query nearby flights.
- Browser geolocation works on `localhost` and secure HTTPS websites. For a hosted deployment, configure an appropriate server and HTTPS.
