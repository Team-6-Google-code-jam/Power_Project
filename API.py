import requests
from datetime import datetime

def get_electricity_prices(dno):
    url = "https://odegdcpnma.execute-api.eu-west-2.amazonaws.com/development/prices"
    
    # Get current date and time
    current_datetime = datetime.now()
    
    # Format the date and time as needed
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
        data = response.json()  # Assuming the response is in JSON format
        return data
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

