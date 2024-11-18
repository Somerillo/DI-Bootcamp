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
        self.geocoding_mgr = self.owm.geocoding_manager()

    def retrieve_weather(self):
        try:
            observation = self.mgr.weather_at_place(self.city)
            # observation = self.mgr.weather_at_id(self.city)
            return observation.weather
        except Exception as e:
            print(f"an error occurred: {e}")
            return None

    def retrieve_geocoding(self):
        try:
            location = self.geocoding_mgr.geocode(self.city)
            return location
        except Exception as e:
            print(f"mistakes were made to geolocation: {e}")
            return None

    def get_temperature(self):
        weather = self.retrieve_weather()
        return weather.temperature("celsius")["temp"] if weather else None

    def get_wind(self):
        weather = self.retrieve_weather()
        return weather.wind() if weather else None

    def get_sunrise_sunset(self):
        weather = self.retrieve_weather()
        if weather:
            sunrise_time = datetime.fromtimestamp(weather.sunrise_time())
            sunset_time = datetime.fromtimestamp(weather.sunset_time())
            return {"sunrise": sunrise_time.strftime('%H:%M:%S'), "sunset": sunset_time.strftime('%H:%M:%S')}
        return None

    def get_reference_time(self):
        weather = self.retrieve_weather()
        return weather.reference_time("iso") if weather else None

    def get_all_data(self):
        weather = self.retrieve_weather()
        if weather:
            return {
                "temperature": weather.temperature("celsius")["temp"],
                "humidity": weather.humidity,
                "status": weather.status,
                "description": weather.detailed_status,
                "wind": weather.wind()
            }
        return None

    def retrieve_air_quality(self):
        try:
            # Get latitude and longitude for the specified city
            location = self.retrieve_geocoding()
            if location:
                air_quality = self.pollution_mgr.air_quality_at_coords(
                    # access the first element of the location list to get latitude and longitude!!!!!!
                    location[0].lat, location[0].lon)
                # print(location)
                return air_quality
            else:
                print("location couldnt benn fetch")
        except Exception as e:
            print(f"An error occurred while retrieveing air quality: {e}")
            return None

    def get_air_quality_data(self):
        air_quality = self.retrieve_air_quality()
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
    
    def get_forecast(self):
        try:
            # Get the weather observation for the specified city
            observation = self.mgr.weather_at_place(self.city)
            lat = observation.location.lat
            lon = observation.location.lon
            
            # Get the forecast for the next 5 days using the coordinates
            one_call = self.mgr.one_call(lat=lat, lon=lon)
            return one_call.forecast_daily[:5]  # Get the first 5 days of forecast
        except Exception as e:
            print(f"An error occurred while retrieving forecast: {e}")
            return None


api_key = 'my-api'

# Create instances for each city
# cities = ["Ashkelon,IL", "Tel Aviv,IL", "Los Angeles,US"]
# weather_instances = [Get_Weather(api_key, city) for city in cities]
cities = ["Ashkelon,IL", "Tel Aviv,IL", "Los Angeles,US"]
city = cities[0]
weather_instances = Get_Weather(api_key, city)

print(weather_instances.get_wind()["speed"])
print(weather_instances.get_temperature())
print(weather_instances.get_sunrise_sunset())
print(weather_instances.get_air_quality_data())


# Obtener y mostrar el pronóstico de los próximos 5 días
forecast_data = weather_instances.get_forecast()
if forecast_data:
    for day in forecast_data:
        print(f"Date: {day.reference_time('iso')}, Temperature: {day.temperature('celsius')['day']}°C")