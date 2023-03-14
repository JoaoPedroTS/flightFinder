import requests
from consts import SHEETY_ENDPOINT, SHEETY_USERNAME, SHEETY_PASSWORD

class DataManager:
    
    def __init__(self) -> None:
        self.destinationData = {}

    def getDestinationData(self):
        response = requests.get(
            url=SHEETY_ENDPOINT,
            auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
        )
        data = response.json()
        self.destinationData = data["prices"]
        return self.destinationData

    def updateDestinationCodes(self):
        for city in self.destinationData:
            newData = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=newData,
                auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
            )

            print(response.text)