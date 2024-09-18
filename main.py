from em import *
import requests as rq
from datetime import datetime
import os

today = datetime.now()
dat= today.strftime('%d/%m/%Y')
tm= today.strftime('%X')

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_header = {
    'Content-Type': 'application/json',
    'x-app-id': NUTRITIONIX_ID,
    'x-app-key': NUTRITIONIX_KEY
}

nutri_param = {
    "query": input("Enter exercise and duration here: ")
}
response = (rq.post(NUTRITIONIX_ENDPOINT, json=nutri_param, headers=nutri_header)).json()
# print(response)

sheety_param = {
    "workout": {
        "date" : dat,
        "time" : tm,
        "exercise" : response["exercises"][0]["name"].title(),
        "duration" : response["exercises"][0]["duration_min"],
        "calories": response["exercises"][0]["nf_calories"],
    },
}

sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

s_response = rq.post(SHEETY_ENDPOINT, json=sheety_param, headers=sheety_header)
print(s_response)


# #No Authentication
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
#
# #Basic Authentication
# sheet_response = requests.post(
#   sheet_endpoint,
#   json=sheet_inputs,
#   auth=(
#       YOUR USERNAME,
#       YOUR PASSWORD,
#   )
# )
#
# #Bearer Token Authentication
# bearer_headers = {
# "Authorization": f"Bearer {YOUR TOKEN}"
# }
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )
