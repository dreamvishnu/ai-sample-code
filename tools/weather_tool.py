from langchain_core.tools import tool
import requests

@tool
def get_temperature(city: str) -> str:
    """
    Get the current temperature (in Celsius) for a given city.
    Example: get_temperature("Mumbai")
    """
    try:
        # Step 1: Geocode city to lat/lon using Open-Meteo geocoding
        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo_resp = requests.get(geo_url).json()
        if "results" not in geo_resp:
            return f"City '{city}' not found."

        lat = geo_resp["results"][0]["latitude"]
        lon = geo_resp["results"][0]["longitude"]

        # Step 2: Get weather data
        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_resp = requests.get(weather_url).json()

        temp = weather_resp.get("current_weather", {}).get("temperature")
        if temp is None:
            return f"Could not fetch temperature for '{city}'."

        return f"The current temperature in {city} is {temp}°C."

    except Exception as e:
        return f"Error: {str(e)}"