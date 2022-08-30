from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Protocol


class Pricing(Protocol):
    def get_total_price(self) -> int:
        ...


@dataclass
class PricePerDay:
    price_per_day: int
    num_days: int

    def get_total_price(self) -> int:
        return self.num_days * self.price_per_day


@dataclass
class PricePerMonth:
    price_per_month: int
    num_months: int

    def get_total_price(self) -> int:
        return self.num_months * self.price_per_month


@dataclass
class PricePerKm:
    price_per_km: int
    num_km: int

    def get_total_price(self) -> int:
        return self.num_km * self.price_per_km


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


class TruckCabStyle(Enum):
    REGULAR = auto()
    EXTENDED = auto()
    CREW = auto()


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    license_plate: str
    reserved: bool
    rates: list[Pricing] = field(default_factory=list)


@dataclass
class Car(Vehicle):
    number_of_seats: int = 5
    storage_capacity_litres: int = 200


@dataclass
class Trailer:
    brand: str
    model: str
    capacity_m3: int
    reserved: bool
    pricing: list[Pricing] = field(default_factory=list)


def default_trailer():
    return Trailer(
        'GE',
        'MBN',
        510,
        True,
        [PricePerDay(10000, 3)]
    )


@dataclass
class Truck(Vehicle):
    cab_style: TruckCabStyle = TruckCabStyle.REGULAR
    trailer: Trailer = default_trailer()


def main():
    truck_a = Truck(
        'GMC', 
        'Mac', 
        'Blue', 
        FuelType.DIESEL, 
        'ABC-123', 
        False,
        sum([PricePerDay(10000, 3).get_total_price()]),
        TruckCabStyle.CREW,
        default_trailer()
    )
    car_b = Car(
        'Honda',
        'Civic',
        'Red',
        FuelType.ELECTRIC,
        'ZXY-987',
        False,
        sum([
            PricePerMonth(300000, 2).get_total_price(), 
            PricePerKm(30, 150000).get_total_price()
        ])
    )
    print(truck_a)
    print(car_b)


if __name__ == "__main__":
    main()
