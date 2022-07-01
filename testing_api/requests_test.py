"""
Some requests to test
"""

import json 
import requests

url = 'https://diabetes-api.herokuapp.com/diabetes_prediction'

input_data_for_model = {
    'Pregnancies' : 1,
    'Glucose' : 85,
    'BloodPressure' : 66,
    'SkinThickness' : 29,
    'Insulin' : 0,
    'BMI' : 26.6,
    'DiabetesPedigreeFunction' :  0.351,
    'Age' : 31
}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(f'{response.text} with the data sent: {input_data_for_model}')


input_data_for_model = {
    'Pregnancies' : 0,
    'Glucose' : 100,
    'BloodPressure' : 80,
    'SkinThickness' : 29,
    'Insulin' : 0,
    'BMI' : 36.6,
    'DiabetesPedigreeFunction' :  0.351,
    'Age' : 31
}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(f'{response.text} with the data sent: {input_data_for_model}')