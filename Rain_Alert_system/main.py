import requests
from twilio.rest import Client

account_sid = "AC9312c63e2d94165d86ee5cd91324333d"
auth_token = "13eaaeef7b39e28c4c990c900de9f800"

parameter={
    "lat":30.32,
    "lon":78.02,
    "appid":"35766afae86f6dd8404d366a1558a203",
    "cnt":4
}
response=requests.get(url="https://api.openweathermap.org/data/2.5/forecast",params=parameter)
response.raise_for_status()
data=response.json()
data=data["list"]
test=False
for x in range(0,len(data)):
    id=data[x]["weather"][0]["id"]
    if id<700:
        test=True
if test:
    # print("Bring Your Umbrella.")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella☔☔",
        from_='+12349013494',
        to='+916396480828'
    )
    print(message.status)