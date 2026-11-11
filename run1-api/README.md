# ISS distance tracker

A small interactive Python program that finds the International Space Station's current position and estimates the distance along Earth's surface from any latitude and longitude you enter. This distance is not a prediction of when the ISS will be visible or pass overhead.

## Run

Use Python 3; no additional packages or API key are needed.

```sh
python3 iss.py
```

Enter coordinates such as `40.44, -79.99` for Pittsburgh. Enter another location to fetch a new position, or `q` to quit. An internet connection is required.

## API

The program uses Python's `urllib.request` to send a GET request to the [Where the ISS at? satellite API](https://www.media.wheretheiss.at/w/developer) for NORAD satellite ID 25544. The `units=kilometers` parameter requests metric units, and omitting a timestamp asks for the current position. The response is JSON, which Python's `json` module converts to a dictionary containing numeric latitude, longitude, altitude, and Unix timestamp fields. The program calculates the great-circle surface distance from your coordinates to the point below the ISS using the haversine formula.

## AI use

Tool: OpenAI Codex. Key prompt: “Find a 15-113 assignment that had to do with APIs. Write a very minimal but complete assignment that satisfies the coding portion, using satellite APIs. DO NOT use the write-good-code skill. Do ALL of your work in a folder called `run1-api`”

This implements the coding portion of 15-113 HW3: Explore an API. Portfolio publication, video, and the submission form are separate assignment deliverables.
