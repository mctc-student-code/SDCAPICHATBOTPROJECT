import requests
import pprint

# https://holidays.abstractapi.com/v1/?api_key=&country=US&year=2025&month=12&day=22 example structure with API key missing
api_key = "" #apit key TODO move to env variable

# User inputs
country = input("Enter country code (e.g., US): ")
year = "2025" # static for now
month = input("Enter month (1-12): ")
day =   input("Enter day (1-31): ")

#TODO: validate user inputs

# Holiday API url without the infor
base_url = "https://holidays.abstractapi.com/v1/?"

# completed URL with user inputs
full_url = f"{base_url}api_key={api_key}&country={country}&year={year}&month={month}&day={day}"


# print(full_url)

response = requests.get(full_url)

print(response.json())
