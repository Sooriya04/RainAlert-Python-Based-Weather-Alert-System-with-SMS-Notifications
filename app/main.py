#GO THROUGH README.md FOR YOUR FOR DOWNLOADING MODULES AND GETTING AN API
from requests import *
from twilio.rest import Client

def send_sms():
    account_sid = "" #YOUR TWILIO ACCOUNT SID
    auth_token = "" #YOUR TWILIO AUTHENTICATION TOKEN
    client = Client(account_sid, auth_token)
    try:
        message = client.messages.create(
            body="Today will be rainny so Don't forgot to get the Umberalla",
            from_= "" , #TWILIO NUMBER
            to="" #YOUR MOBILE NUMBER
        )
    except Exception as e:
        print(f"Error: {e}")

lat = #your lat
long = #your log
api_key = "" #your api key
params = {
    'lat': lat,
    'lon': long,
    'appid': api_key,
    }
api = get(url = "https://api.openweathermap.org/data/2.5/weather?", params = params)
data_file = api.json()
data = data_file["weather"][0]["main"]
if data == "Rain":
    send_sms()
    print("SMS is send")
