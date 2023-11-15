import requests

url = 'http://127.0.0.1:8000/get_form'
data = {
    'customer_email': 'john.dow@home.local',
    'full_name': 'john dow',
    'phone': '+7 456 789 12 43',
    'date': '2023-11-15'
}

result = requests.post(url, data=data)
print(result.text, result.status_code)
