import requests
import datetime
import os


today = datetime.datetime.now()

# Nutritionix settings
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
print(API_KEY)
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": '0'
}
Nutri_endpoint = "https://trackapi.nutritionix.com"
EXERCISE_ENDPOINT = f"{Nutri_endpoint}/v2/natural/exercise"

# Sheety settings
SHEETY_ENDPOINT = "https://api.sheety.co/20fd282edf1d8f04dd1d803352d705b0/myWorkouts/workouts"



post_inf = {
    "query": input("Tell me which exercise you did"),
    "gender": "male",
    "weight_kg": 67.5,
    "height_cm": 170.05,
    "age": 23
}
post_inf = requests.post(url=EXERCISE_ENDPOINT, json=post_inf, headers=HEADERS)
result = post_inf.json()
#print(result)

for data in result['exercises']:
    add_row = {
            "workout": {
                "date": today.strftime("%d/%m/%Y"),
                "time": today.strftime("%H:%M:%S"),
                "exercise": data["name"].title(),
                "duration": data["duration_min"],
                "calories": data["nf_calories"]
            }
    }
    authorization = "u1)dUdPS6Xo&"
    header_sheety = {"Authorization": "Bearer" + authorization}
    response = requests.post(url=SHEETY_ENDPOINT, json=add_row, headers=header_sheety)
