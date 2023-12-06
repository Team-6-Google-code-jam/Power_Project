import json
import requests
from datetime import datetime

def get_electricity_prices(dno):
    url = "https://odegdcpnma.execute-api.eu-west-2.amazonaws.com/development/prices"

    current_datetime = datetime.now()
    
    start_date = current_datetime.strftime("%d-%m-%Y")
    end_date = current_datetime.strftime("%d-%m-%Y")

    params = {
        'dno': str(dno),
        'voltage': 'LV',
        'start': start_date,
        'end': end_date
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()  
        return data
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

