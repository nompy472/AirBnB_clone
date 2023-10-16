#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents User.

    Attributes:
        email (str): User email
        password (str): User password
        first_name (str): User firstname
        last_name (str): User last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""