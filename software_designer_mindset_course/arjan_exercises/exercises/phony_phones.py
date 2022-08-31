from dataclasses import dataclass
from datetime import date
from enum import auto, Enum


class PhoneBrand(Enum):
    SAMSUNG: auto()
    APPLE: auto()
    PLUS_ONE: auto()


@dataclass
class Customer:
    name: str
    address: str
    email_addy: str


@dataclass
class Phone:
    brand: PhoneBrand
    model: str
    price: int
    serial_number: str


@dataclass
class Plan:
    customer: Customer
    phone: Phone
    start_date: date
    length_in_months: int
    monthly_rate: int
    phone_included: bool = False

