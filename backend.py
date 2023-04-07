import requests

API_key="c6a047941a3667a037c75bc60ba38166"
def get_data(place,forecast_days=None,kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filter_data = data["List"]
    nr_value = 8*forecast_days
    filter_data = filter_data[:nr_value]
    if kind == "Temperature":
        filter_data = [dict["main"]["temp"] for dict in filter_data]
    if kind == "sky":
        filter_data = [dict["weather"][0]["main"] for dict in filter_data]
    return filter_data

if __name__=="___main__":
    get_data(place="tokyo", forecast_days=3,kind="sky")