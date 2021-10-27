from .foundation import bookshelf, amadeus_client
from amadeus.client.errors import ResponseError, ClientError
from .errors import AmadeusBadRequest


class AvailabilitySearch:

    def __init__(self: object, departure_iata: str, arrival_iata: str, date: str) -> object:
        self.__departure_iata = departure_iata
        self.__arrival_iata = arrival_iata
        self.__date = date

    def go(self: object) -> list:
        # load availabilities
        try:
            response = amadeus_client.shopping.availability.flight_availabilities.post(
                {
                    "originDestinations": [
                        {
                            "id": "1",
                            "originLocationCode": self.__departure_iata,
                            "destinationLocationCode": self.__arrival_iata,
                            "departureDateTime": {
                                "date": self.__date
                            },
                        },
                    ],
                    "travelers": [
                        {
                            "id": "1",
                            "travelerType": "ADULT",
                        },
                    ],
                    "sources": [
                        "GDS",
                    ],
                },
            )
        except ResponseError:
            print(1)
            raise AmadeusBadRequest
        except ClientError:
            print(2)
            raise AmadeusBadRequest

        # save dictionaries
        dictionaries = response.result['dictionaries']
        bookshelf.add(**dictionaries)

        availabilities = response.result['data']

        slim_availabilities = self.__simplify_availabilities(availabilities)
        return slim_availabilities

    def __simplify_availabilities(self: object, availabilities: list) -> dict:
        simplified_availabilities = dict()
        for a in availabilities:
            # go for only non-stop
            if len(a['segments']) != 1:
                continue
            # extract the only segment
            # tos: the only segment
            the_only_segment = a['segments'][0]
            flight_number = the_only_segment['carrierCode'] + \
                the_only_segment['number']

            simplified_availabilities[flight_number] = {
                c['class']: c['numberOfBookableSeats'] for c in the_only_segment['availabilityClasses']
            }
        return simplified_availabilities
