from dataclasses import dataclass
from enum import Enum, auto


class VehicleType(Enum):
    VW = auto()
    BMW = auto()
    FORD = auto()


@dataclass
class VehicleData:
    """A class to hold vehicle data."""

    brand: str
    price_per_day: int
    price_per_km: int
    rental_cost = None

    def compute_rental_cost(self, km, days) -> int:
        """Computes the rental cost for a vehicle."""
        price_per_km = self.price_per_km
        price_per_day = self.price_per_day
        # TODO remove this
        paid_kms = max(km - 100, 0)
        # TODO you don't pay for the first 100 km... make this a property
        self.rental_cost = price_per_km * paid_kms + price_per_day * days


VEHICLE_DATA = {
    "VW": VehicleData(brand="vw", price_per_km=30, price_per_day=6000),
    "BMW": VehicleData(brand="bmw", price_per_km=35, price_per_day=8500),
    "FORD": VehicleData(brand="ford", price_per_km=25, price_per_day=12000),
}


def read_vehicle_type() -> str:
    """Reads the vehicle type from the user."""
    vehicle_type = ""
    while vehicle_type not in VehicleType._member_names_:
        vehicle_type = input(
            f"What type of vehicle would you like to rent ({', '.join(VehicleType._member_names_)})? "
        )
    return vehicle_type


def read_rent_days() -> int:
    """Reads the number of days from the user."""
    days = 0
    while days < 1:
        days_str = input(
            "How many days would you like to rent the vehicle? (enter a positive number) "
        )
        try:
            days = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return days


def read_kms_to_drive() -> int:
    """Reads the number of kilometers to drive from the user."""
    km = 0
    while km < 1:
        km_str = input(
            "How many kilometers would you like to drive (enter a positive number)? "
        )
        try:
            km = int(km_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return km


def main():
    vehicle_type = read_vehicle_type()
    # Might need to make days and km class attrs of the vehicle
    days = read_rent_days()
    km = read_kms_to_drive()

    vehicle = VEHICLE_DATA[vehicle_type]
    # compute the final rental price
    vehicle.compute_rental_cost(days, km)

    # print the result
    print(f"The total price of the rental is ${(vehicle.rental_cost / 100):.2f}")


if __name__ == "__main__":
    main()
