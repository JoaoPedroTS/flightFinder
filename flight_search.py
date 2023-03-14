import requests

from flight_data import FlightData
from consts import TEQUILA_ENDPOINT, TEQUIlA_API_KEY

class FlightSearch:
    
    def __init__(self) -> None:
        self.header = {
            "apikey": TEQUIlA_API_KEY,
        }
    
    def getDestinationCode(self, city):
        
        params = {
            "term": city,
            "location_type": "city",
        }

        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/locations/query",
            headers=self.header,
            params=params
        )

        data = response.json()["locations"]
        code = data[0]["code"]
        return code

    def getFlights(self, origin, destination, fromTime, toTime):
        searchEndpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        parameters = {
            "fly_from": origin,
            "fly_to": destination,
            "date_from": fromTime.strftime("%d/%m/%Y"),
            "date_to": toTime.strftime("%d/%m/%Y"),
            "max_stopovers": 0,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
        }

        response = requests.get(
            url=searchEndpoint,
            headers=self.header,
            params=parameters
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination}")
            return None

        flightData = FlightData(
            price=data["price"],
            originCity=data["route"][0]["cityFrom"],
            originAirport=data["route"][0]["flyFrom"],
            destinationCity=data["route"][0]["cityTo"],
            destinationAirport=data["route"][0]["flyTo"],
            outDate=data["route"][0]["local_departure"].split("T")[0],
            returnDate=data["route"][1]["local_departure"].split("T")[0]
        )

        return flightData