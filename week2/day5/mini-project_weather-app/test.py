# # this is direct from the api page module and it doesnt work :(

# from pyowm.owm import OWM

# api_key = 'e9a9304081c135f075a0b0f220e29980'

# owm = OWM(api_key)
# mgr = owm.weather_manager()
# one_call = mgr.one_call(lat=52.5244, lon=13.4105)

# print(one_call.forecast_daily[0].temperature('celsius').get('feels_like_morn', None))



import requests

def obtener_pronostico(api_key, latitud, longitud):
    url = "https://api.tomorrow.io/v4/timelines"
    params = {
        "location": f"{latitud},{longitud}",
        # "fields": ["temperature", "precipitationProbability", "humidity", "windSpeed"],
        "fields": ["temperature", "precipitationProbability", "humidity", "windSpeed"],
        "units": "metric",
        "timesteps": "1d",
        "startTime": "now",
        "endTime": "nowPlus5d",
        "apikey": api_key
    }

    try:
        respuesta = requests.get(url, params=params)
        respuesta.raise_for_status()  # Lanza un error para respuestas no exitosas
        datos = respuesta.json()
        return datos
    except requests.exceptions.RequestException as e:
        print(f'Error al obtener el pronóstico: {e}')
        return None

def imprimir_pronostico(pronostico):
    if pronostico and 'data' in pronostico:
        timeline = pronostico['data']['timelines'][0]
        print(f"Pronóstico de los próximos 5 días:")
        for intervalo in timeline['intervals']:
            fecha = intervalo['startTime']
            valores = intervalo['values']
            print(f"Fecha: {fecha}")
            print(f"  Temperatura: {valores['temperature']} °C")
            print(f"  Humedad: {valores['humidity']} %")
            print(f"  Probabilidad de Precipitación: {valores['precipitationProbability']} %")
            print(f"  Velocidad del Viento: {valores['windSpeed']} m/s")
            print("-" * 40)

# Ejemplo de uso
api_key = 'my-api'  # Reemplaza con tu clave de API
latitud = 40.7128  # Latitud de Nueva York
longitud = -74.0060  # Longitud de Nueva York

pronostico = obtener_pronostico(api_key, latitud, longitud)
imprimir_pronostico(pronostico)
