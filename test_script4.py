import requests

url = 'http://127.0.0.1:8000/get_form'
data = {
    'some_email': 'john.dow@home.local',
    'my_name': 'john dow',
    'mob_phone': '+7 456 789 12 43',
    'dob': '15.05.1995'
}

result = requests.post(url, data=data)
print(result.text, result.status_code)
