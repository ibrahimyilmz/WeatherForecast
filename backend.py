import requests
from datetime import datetime, timedelta

API_KEY = '9bbd2f913f14f1d88851bdb5d7c400bc'

def get_data (place="Ankara", forecast_days=None, kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    temperatures = []
    icon_urls = []
    dates = []

    # Calculate the end date based on the forecast_days
    # To only show the desired days in webpage
    end_date = datetime.now() + timedelta(days=forecast_days)

    for dic in filtered_data:
        # Convert the date in the data to a datetime object
        datetime_obj = datetime.strptime(dic["dt_txt"], "%Y-%m-%d %H:%M:%S")

        if datetime_obj <= end_date:
            # Converting data into format that will be used on webpage
            dates.append(datetime_obj.strftime("%Y-%m-%d %H:%M"))
            # Converting temperature into Celsius format
            temp = dic["main"]["temp"] - 273.15
            temperatures.append(f"{temp:.1f}")

            if kind == "Sky":
                icon_url = f"https://openweathermap.org/img/wn/{dic['weather'][0]['icon']}@2x.png"
                icon_urls.append(icon_url)

    return dates, temperatures, icon_urls

if __name__ == '__main__':
    print(get_data(place="Ankara"))