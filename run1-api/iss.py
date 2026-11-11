"""Find the ISS and its approximate surface distance from a location."""
import json
import math
from datetime import datetime, timezone
from urllib.error import URLError
from urllib.request import urlopen

API_URL = "https://api.wheretheiss.at/v1/satellites/25544?units=kilometers"


def coordinates(text):
    parts = text.split(",")
    if len(parts) != 2:
        raise ValueError("Enter latitude, longitude (for example, 40.44, -79.99).")
    try:
        lat, lon = (float(part) for part in parts)
    except ValueError:
        raise ValueError("Latitude and longitude must be numbers.") from None
    if not (-90 <= lat <= 90 and -180 <= lon <= 180):
        raise ValueError("Latitude must be -90 to 90 and longitude -180 to 180.")
    return lat, lon


def surface_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, (lat1, lon1, lat2, lon2))
    a = math.sin((lat2 - lat1) / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin((lon2 - lon1) / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(min(1, a)))


def show_iss(lat, lon):
    try:
        with urlopen(API_URL, timeout=10) as response:
            data = json.load(response)
        iss_lat, iss_lon = float(data["latitude"]), float(data["longitude"])
        distance = surface_distance(lat, lon, iss_lat, iss_lon)
        timestamp = datetime.fromtimestamp(data["timestamp"], timezone.utc)
        print(f"ISS at {iss_lat:.2f}°, {iss_lon:.2f}°; altitude {data['altitude']:.0f} km")
        print(f"Surface distance from your location: {distance:,.0f} km")
        print(f"Position time: {timestamp:%Y-%m-%d %H:%M:%S UTC}")
        print("Surface distance is not a visibility or overhead-pass prediction.")
    except (URLError, TimeoutError, OSError, ValueError, KeyError, TypeError, OverflowError):
        print("Could not retrieve a valid ISS position. Check your connection and try again.")


def main():
    print("ISS distance tracker. Enter q to quit.")
    while True:
        try:
            text = input("Your latitude, longitude: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if text.lower() == "q":
            break
        try:
            lat, lon = coordinates(text)
        except ValueError as error:
            print(error)
            continue
        show_iss(lat, lon)


if __name__ == "__main__":
    main()
