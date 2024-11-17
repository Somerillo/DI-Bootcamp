# Building a Weather App

# The current weather data can be retrieved from OpenWeatherMap using the Observation module in PyOWM (Python OpenWeatherMap).
# Use this documentation[https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html#weather_data] for this Mini Project.

# 1     Get the current weather in Tel Aviv.
# 2     Get current wind info of Tel Aviv.
# 3     Get today’s sunrise and sunset times of Tel Aviv.
# 4     Display all these information in a user friendly way.


from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from datetime import datetime


class Get_Weather:
    def __init__(self, api_key, city="Ashkelon,IL"):
        self.city = city
        self.owm = OWM(api_key)
        self.mgr = self.owm.weather_manager()
        self.pollution_mgr = self.owm.airpollution_manager()

    def fetch_weather(self):
        try:
            observation = self.mgr.weather_at_place(self.city)
            # observation = self.mgr.weather_at_id(self.city)
            return observation.weather
        except Exception as e:
            print(f"an error occurred: {e}")
            return None

    def get_temperature(self):
        weather = self.fetch_weather()
        return weather.temperature("celsius")["temp"] if weather else None

    def get_wind(self):
        weather = self.fetch_weather()
        return weather.wind() if weather else None

    def get_sunrise_sunset(self):
        weather = self.fetch_weather()
        if weather:
            sunrise_time = datetime.fromtimestamp(weather.sunrise_time())
            sunset_time = datetime.fromtimestamp(weather.sunset_time())
            return {"sunrise": sunrise_time.strftime('%H:%M:%S'), "sunset": sunset_time.strftime('%H:%M:%S')}
        return None

    def get_reference_time(self):
        weather = self.fetch_weather()
        return weather.reference_time("iso") if weather else None

    def get_all_data(self):
        weather = self.fetch_weather()
        if weather:
            return {
                "temperature": weather.temperature("celsius")["temp"],
                "humidity": weather.humidity,
                "status": weather.status,
                "description": weather.detailed_status,
                "wind": weather.wind()
            }
        return None
    
    def fetch_air_quality(self):
        try:
            # Get latitude and longitude for the specified city
            reg = self.owm.city_id_registry()
            loc = reg.locations_for(self.city.split(",")[0], country=self.city.split(",")[1])[0]
            air_quality = self.pollution_mgr.air_quality_at_coords(loc.lat, loc.lon)
            return air_quality
        except Exception as e:
            print(f"An error occurred while fetching air quality: {e}")
            return None

    def get_air_quality_data(self):
        air_quality = self.fetch_air_quality()
        if air_quality:
            return {
                "aqi": air_quality.aqi,
                "co": air_quality.co,
                "no": air_quality.no,
                "no2": air_quality.no2,
                "o3": air_quality.o3,
                "so2": air_quality.so2,
                "pm2_5": air_quality.pm2_5,
                "pm10": air_quality.pm10,
                "nh3": air_quality.nh3
            }
        return None


api_key = 'e9a9304081c135f075a0b0f220e29980'

# Create instances for each city
cities = ["Ashkelon,IL", "Tel Aviv,IL", "Los Angeles,US"]
weather_instances = [Get_Weather(api_key, city) for city in cities]

# Display date, time, temperature, sunrise & sunset for each city
for weather in weather_instances:
    temp = weather.get_temperature()
    wind = weather.get_wind()
    sunrise_sunset = weather.get_sunrise_sunset()
    reference_time = weather.get_reference_time()
    air_quality = weather.get_air_quality_data()

    print(f"City: {weather.city}")
    print(f"Date and Time: {reference_time}")
    print(f"Temperature: {temp:.1f}°C")
    print(f"Wind: {wind["speed"]} km/h")
    print(f"Sunrise: {sunrise_sunset["sunrise"]}")
    print(f"Sunset: {sunrise_sunset["sunset"]}")

    if air_quality:
        print("Air Quality Index (AQI):", air_quality["aqi"])
        print("CO:", air_quality["co"], "μg/m3")
        print("NO:", air_quality["no"], "μg/m3")
        print("NO2:", air_quality["no2"], "μg/m3")
        print("O3:", air_quality["o3"], "μg/m3")
        print("SO2:", air_quality["so2"], "μg/m3")
        print("PM2.5:", air_quality["pm2_5"], "μg/m3")
        print("PM10:", air_quality["pm10"], "μg/m3")
        print("NH3:", air_quality["nh3"], "μg/m3")
    else:
        print("Air Quality: Data not available")

    print("-" * 30)
