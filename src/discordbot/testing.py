import settings
# importing the requests library
import requests

url = "https://api.starcitizen-api.com/"

STAR_CITIZEN_TOOLS_TOKEN = settings.STAR_CITIZEN_TOOLS_API_SECRET

#/v1/live/ships?classification=multi&classification=combat&page_max=1&price_max=50 HTTP/1.
#GET /xxxxxxxx/v1/live/ships?classification=multi&classification=combat&page_max=1&price_max=50 HTTP/1.

ROADMAP = "/v1/cache/roadmap/starcitizen"
STAR_SYSTEM = "/v1/cache/starmap/systems?name=Stanton"

GET_ROADMAP = url + STAR_CITIZEN_TOOLS_TOKEN + ROADMAP
GET_STAR_SYSTEM = url + STAR_CITIZEN_TOOLS_TOKEN + STAR_SYSTEM

# A GET request to the API
# response = requests.get(url + STAR_CITIZEN_TOOLS_TOKEN + ROADMAP)

response = requests.get(GET_STAR_SYSTEM)
print(GET_STAR_SYSTEM)
# Print the response
response_json = response.json()
# print(response_json["data"]["name"])
#print(response_json)