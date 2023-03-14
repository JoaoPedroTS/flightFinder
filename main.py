from datetime import datetime, timedelta

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_CODE = "LON"

dataManager = DataManager()
sheetData = dataManager.getDestinationData()

flightSearch = FlightSearch()

notificationManager = NotificationManager()


if sheetData[0]["iataCode"] == "":
    for row in sheetData:
        row["iataCode"] = flightSearch.getDestinationCode(row["city"])

    dataManager.destinationData = sheetData
    dataManager.updateDestinationCodes()

today = datetime.now()
tomorrow = today + timedelta(days=1)
sixMonthsTime = today + timedelta(days=(6*30))

for destination in sheetData:
    flight = flightSearch.getFlights(
        ORIGIN_CITY_CODE,
        destination["iataCode"],
        fromTime= tomorrow,
        toTime=sixMonthsTime
    )

    if flight is None:
        continue


    if flight.price < destination["lowestPrice"]:
        # notificationManager.sendSMS(
        #     message=f"Low price alert! Only £{flight.price} to fly from {flight.originCity} - {flight.originAirport} to {flight.destinationCity} - {flight.destinationAirport}, from {flight.outDate} to {flight.returnDate}"
        # )

        print(f"Low price alert! Only £{flight.price} to fly from {flight.originCity} - {flight.originAirport} to {flight.destinationCity} - {flight.destinationAirport}, from {flight.outDate} to {flight.returnDate}")