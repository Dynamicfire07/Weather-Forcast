import requests
api_key = "3641f9e83082b01d470c7d1c6841f31a"
def get_data(place,forcast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_value = 8*forcast_days
    filtered_data = filtered_data[:nr_value]
    return filtered_data

if __name__ == "__main__":
     print(get_data(place="Mumbai",forcast_days=3))