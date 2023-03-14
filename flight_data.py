class FlightData:
    
    def __init__ (
            self,
            price,
            originCity,
            originAirport,
            destinationCity,
            destinationAirport,
            outDate,
            returnDate,
            stopOvers = 0,
            viaCity = ""
        ) -> None:
        self.price = price
        self.originCity = originCity
        self.originAirport = originAirport
        self.destinationCity = destinationCity
        self.destinationAirport = destinationAirport
        self.outDate = outDate
        self.returnDate = returnDate
        self.stopOvers = stopOvers
        self.viaCity = viaCity