import requests
import smtplib

api_key = "************"

weather_params = {
    "lat": 40.7143,
    "lon": -74.006,
    "units": "imperial",
    "appid": api_key,
    "exclude": "current,daily,minutely"

}


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
raw_data = response.json()
NYC_weather_hourly = raw_data["hourly"][0:12]

will_rain = False

for hour_data in NYC_weather_hourly:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    my_email = "*****************"
    password = "*****************"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="nostro37@gmail.com",
                            msg=f"Subject:Umbrella reminder\n\nLooks like it's going to rain. Don't forget your umbrella!")
