from __future__ import annotations
from datetime import datetime
import os

class Flight:
    origin = None
    destination = None
    departure = None
    arrival = None
    price = None

    def __init__(self,
                 origin: str = None,
                 destination: str = None,
                 departure: datetime.time = None,
                 arrival: datetime.time = None,
                 price: float = None):
        self.origin = origin
        self.destination = destination
        self.departure = departure
        self.arrival = arrival
        self.price = price


def load_flights(flights_path) -> list[Flight]:
    flights = []
    for line in open(flights_path, 'r'):
        split = line.split(",")
        flights.append(Flight(
            split[0],
            split[1],
            datetime.strptime(split[2], "%H:%M"),
            datetime.strptime(split[3], "%H:%M"),
            float(split[4])
        ))
    return flights

if __name__ == '__main__':
    pass
    #print(load_flights(os.getcwd()+'/data/flights.txt'))