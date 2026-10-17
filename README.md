# ✈️ Sky Above Me

**A personal flight tracker showing aircraft flying near you.**

Sky Above Me is a lightweight, mobile-friendly flight tracking website that displays nearby aircraft, their flight information and airline details.

🌐 **[Launch Sky Above Me](https://gretaruby-coder.github.io/flight-tracker/)**

## Features

- ✈️ View aircraft flying near your selected location.
- 📍 Calculate the distance between you and nearby aircraft.
- 📏 Adjust the search radius.
- 🛫 Display callsigns, airlines, aircraft types and registrations.
- 🧭 View altitude, speed and heading.
- 🌍 Display departure and destination information when available.
- 🔄 Refresh aircraft information automatically when updated data is available.
- 📱 Responsive interface for desktop, tablet and mobile.
- 🎮 Demo mode for exploring the interface.

## How It Works

Sky Above Me uses publicly available ADS-B aircraft tracking data.

1. A GitHub Actions workflow retrieves aircraft positions from the ADS-B API.
2. The workflow processes the aircraft data and saves it to `aircraft.json`.
3. GitHub Pages hosts the website and its data files.
4. The website checks for updated aircraft information every 30 seconds.
5. Aircraft within the selected radius are displayed.

**Note:** The website's refresh interval is separate from the data collection interval. Live aircraft positions depend on successful backend updates and data availability.

## Technologies

- HTML, CSS and JavaScript
- GitHub Pages
- GitHub Actions
- ADS-B aircraft tracking API
- JSON

## Project Structure

```text
flight-tracker/
├── index.html
├── aircraft.json
├── routes-cache.json
├── logos/
├── .github/
│   └── workflows/
│       └── update-aircraft.yml
└── README.md
```

## Aircraft Data

Aircraft positions are retrieved from the [adsb.fi Open Data API](https://opendata.adsb.fi/).

Flight route information may be enriched using additional publicly available data.

Aircraft information can be delayed, incomplete or temporarily unavailable depending on API coverage and update frequency.

## Automatic Updates

The project uses a GitHub Actions workflow called **Update Aircraft Data**.

The workflow supports manual execution and is intended to run on a five-minute schedule.

GitHub Actions scheduled executions are not guaranteed to occur at an exact time and may be delayed or missed.

## Purpose

Sky Above Me is a personal project built to make it easy to identify aircraft passing overhead without needing a full flight tracking platform.

The website is intended for informational and recreational use only.

---

Made with curiosity for aviation. ✈️
