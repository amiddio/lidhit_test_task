import requests

url = 'http://127.0.0.1:8000/get_form'
data = {
    'customer_email': 'john.dow@home.local',
    'first_name': 'john',
    'last_name': 'dow',
    'customer_phone': '+7 456 789 12 43',
    'customer_dob': '01.03.1981',
    'gender': 'male',
}

result = requests.post(url, data=data)
print(result.text, result.status_code)
