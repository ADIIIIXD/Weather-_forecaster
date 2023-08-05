import requests

API_KEY = "06e6c7afc2f4dc2cd5a0ae622d3884a6"


def get_data(place, days):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[0:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="London", days=2))

