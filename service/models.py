"""Data model for customer accounts."""

from dataclasses import dataclass


@dataclass
class Account:
    """Represent a customer account."""

    name: str
    email: str
    address: str
    phone_number: str
    date_joined: str
