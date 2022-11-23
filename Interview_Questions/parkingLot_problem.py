#!/usr/bin/python3
"""
Code Challenge - Parking lot
    Design a parking lot using object-oriented principles

Assumptions:
    - The parking lot can hold motorcycles, cars and vans
    - The parking lot has small spots, medium spots and large spots.
    - A motorcycle can park in any spot.
    - A car can park in a medium spot, or a large spot.
    - A van can park only in a large spot.
    - Only 1 motorcycles can fit in a small spot
    - 2 motorcycles can fit in 1 medium spot.
    - 4 motorcycles can fit in 1 large spot.
    - Only 1 car can fit in a medium spot.
    - 2 cars can fit in a large spot.
    - Only 1 van can fit in a large spot.

Functionality needed:
    - Ability to add vehicles by type. Once added it should deduct accordingly from total slots.
    - Ability to tell us how many spots are remaining by vehicle type or by all types.
    - Ability to tell us if the lot is full.

Your solution:
    You can add any classes or methods you would like to display your solution.
    Display best practices using object oriented programming.
    Please submit your code by a zip file.

"""


class ParkingLot:
    def __init__(self, smallspots, mediumspots, largespots) -> None:
        self.smallspotRemaing = smallspots
        self.medspotRemaing = mediumspots
        self.largspotRemaing = largespots

    def add_vehicle(self, vehicletype) -> str:
        """Ability to add vehicles by type. Once added it should deduct accordingly from total slots."""
        print(f"trying to add {vehicletype}")
        if vehicletype == "motorcycle":
            if self.smallspotRemaing >= 1:
                self.smallspotRemaing -= 1  # 1 motorcycles can fit in a small spot
            elif self.medspotRemaing >= 0.5:
                self.medspotRemaing -= 0.5  # 2 motorcycles can fit in 1 medium spot
            elif self.largspotRemaing >= 0.25:
                self.largspotRemaing -= 0.25  # 4 motorcycles can fit in 1 large spot
            else:
                return "no parking for motorcycle"

        elif vehicletype == "car":
            if self.medspotRemaing >= 1:
                self.medspotRemaing -= 1  # 1 car can fit in a medium spot.
            elif self.largspotRemaing >= 0.5:
                self.largspotRemaing -= 0.5  # 2 cars can fit in a large spot
            else:
                return "no parking for car"

        elif vehicletype == "van":
            if self.largspotRemaing >= 1:
                self.largspotRemaing -= 1
            else:
                return "no parking for van"
        else:
            return f"Invalid vehicle type: {vehicletype}"

        return "Reserved"

    def current_parking_status(self):
        """Ability to tell us how many spots are remaining by vehicle type or by all types."""
        print(
            f"""
        CURRENT STATUS
            SPOT-WISE Availability:
                smallspots : {self.smallspotRemaing}
                mediumspots: {self.medspotRemaing}
                largespots : {self.largspotRemaing}

            VEHICLE-WISE Availability:
                motorcycles: {self.smallspotRemaing + self.medspotRemaing * 2 + self.largspotRemaing * 4}
                cars       : {self.medspotRemaing + self.largspotRemaing * 2}
                vans       : {self.largspotRemaing}
        """
        )

    def is_parking_full(self):
        """Ability to tell us if the lot is full."""
        return self.smallspotRemaing == self.medspotRemaing == self.largspotRemaing == 0


if __name__ == "__main__":
    pl = ParkingLot(smallspots=10, mediumspots=5, largespots=2)
    print(pl.add_vehicle("motorcycle"))
    pl.current_parking_status()

    print(pl.add_vehicle("motorcycle"))
    print(pl.add_vehicle("motorcycle"))
    pl.current_parking_status()
    pl.is_parking_full()

    print(pl.add_vehicle("car"))
    print(pl.add_vehicle("van"))
    print(pl.add_vehicle("car"))
    pl.is_parking_full()


"""
OUTPUT:
=======
trying to add motorcycle
Reserved

        CURRENT STATUS
            SPOT-WISE Availability:
                smallspots : 9
                mediumspots: 5
                largespots : 2

            VEHICLE-WISE Availability:
                motorcycles: 27
                cars       : 9
                vans       : 2

trying to add motorcycle
Reserved
trying to add motorcycle
Reserved

        CURRENT STATUS
            SPOT-WISE Availability:
                smallspots : 7
                mediumspots: 5
                largespots : 2

            VEHICLE-WISE Availability:
                motorcycles: 25
                cars       : 9
                vans       : 2

trying to add car
Reserved
trying to add van
Reserved
trying to add car
Reserved

"""
