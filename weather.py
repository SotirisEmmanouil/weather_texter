import schedule 
import time

def get_weather(latitude,longitude):
    base_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
    repsonse = request.get(base_url)
    data = response.json()
    return data  #fetch data from API

def celcius_to_fahrenheit(celcius):
    return (celcius * 9/5) * 32
       

def send_weather_update():
    #hard coded coordinates for NYC
    latitude =40.7128
    latitude = -74.0060

    weather_data = get_weather(latitude, longitude)
    temperature_celcius = weather_data["hourly"]["temperature_2m"][0]
    relativehumidity = weather_data["hourly"]["relativehumidity_2m"][0]
    wind_speed = weather_data["hourly"]["windspeed_10m"][0]
    temperature_fahrenheit = celcius_to_fahrenheit(temperature_celcius)

    weather_info = (
            f"Good morning!\n"
            f"Current weather in New York City:\n"
            f"Temperature: {temperature_fahrenheit:.2f}F\n"
            f"Relative Humidity: {relative_humidity}%\n"
            f"Wind Speed {wind_speed} m/s"

        )       #the actual message 
    send_text_message(weather_info)     #send the message
    
def send_text_message(body):
    account_sid = "twilio_sid"
    auth_token = "twilio_token"
    from_phone_number = "3476022509"
    to_phone_number = "3476022509"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = body,
        from_= from_phone_number,
        to = to_phone_number
    )
    print("Text message sent!")
                

def main():
    schedule.every().day.at("12:19").do(send_weather_update) #send update every day at that time
    while True:
        schedule.run_pending()
        time.sleep(1)       #once a day

if __name__ == "__main__":
    main()
