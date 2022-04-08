"""
Company             : bloomberg
Problem statement   : Average Journey Time

    Transport for London
    entrance(card_id: int, station: str, timestamp: datetime)
    exit(card_id: int, station: str, timestamp: datetime)
    get_average_journey_time(start_station: str, end_station: str)

    entrance(42, "Liverpool Street", datetime.now())
    entrance(84, "Bank", datetime.now())
    exit(42, "Oxford Circus", datetime.now())
    exit(84, "Oxford Circus", datetime.now())

"""
from datetime import datetime


class Transport(object):
    def __init__(self) -> None:
        self.live_journeys = {}  # cardId: (startStn, startTime)
        self.journey_duration = {}   # sourcestn-dest_stn: duration

    def entrance(self, card_id: int, station: str, timestamp: datetime):
        self.live_journeys[card_id] = (station, timestamp)   # O(1)

    def exit(self, card_id: int, station: str, timestamp: datetime):
        if not card_id in self.live_journeys:  # O(1)
            return
        startStn, startTime = self.live_journeys.pop(card_id)

        strt_end_stns = (startStn, station)
        curr_duration = timestamp - startTime

        if strt_end_stns in self.journey_duration:
            existing_duration, exiting_count = self.journey_duration[strt_end_stns]
            self.journey_duration[strt_end_stns] = [
                existing_duration + curr_duration, exiting_count + 1]
        else:
            self.journey_duration[strt_end_stns] = [curr_duration, 1]

    def get_average_journey_time(self, start_station: str, end_station: str):     # O(1)
        if (start_station, end_station) in self.journey_duration:
            durationsSum, Counts = self.journey_duration[(
                start_station, end_station)]
            print(durationsSum / Counts)
        else:
            print('dont know')

# lt = Transport()
# lt.get_average_journey_time("Oxford Circus", "Liverpool Street")

# Start Station = "A-B", End Station = "C"
# Start Station = "A", End Station = "B-C"
# Start Station = "A~B", End Station = "C"
# Start Station = "A", End Station = "B~C"
# Start Station = "A-B", End Station = "C"
# Start Station = "AB", End Station = "C"

# Incorrect data types
# Exit but no entrance
# Entrance but no exit
# Incorrect station IDs
# Multiple entrances & exits
# Larger-scale averaging
# delimiter in station names


lt = Transport()
lt.entrance(42, "Liverpool Street", datetime.now())
lt.entrance(84, "Bank", datetime.now())
lt.exit(42, "Oxford Circus", datetime.now())
lt.exit(84, "Oxford Circus", datetime.now())

lt.get_average_journey_time("Liverpool Street", "Oxford Circus")
