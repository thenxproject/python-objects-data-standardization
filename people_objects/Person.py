import re

from openpyxl.pivot import record


class Person:
    def __init__(self,
                 first_name: str = "",
                 last_name: str = "",
                 street_address: str = "",
                 unit: str = "",
                 city: str = "",
                 state: str = "",
                 zip_code: str = "",
                 phone_number: str = "",
                 email: str = ""):
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.street_address: str = street_address
        self.unit: str = unit
        self.city: str = city
        self.state: str = state
        self.zip_code: str = zip_code
        self.phone_number: str = phone_number
        self.email: str = email

    def set(self, name: str, value: any):
        """Sets the value of a property."""

        self.__setattr__(name, value)

    def get(self, name: str):
        """Gets the value of a property."""

        return self.__getattribute__(name)

    def get_unformatted_phone(self) -> str:
        """Does a regex substitution to replace formatting characters."""

        return re.sub(r"[()\-. ]", "", str(self.phone_number))

    def get_formatted_phone(self) -> str:
        """Gets a phone number formatted as (###) ###-####."""

        phone = self.get_unformatted_phone()
        return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}" if len(phone) == 10 else phone

    def get_full_name(self) -> str:
        """Gets the full name in the format FirstName LastName."""

        return f"{self.first_name} {self.last_name}"

    def get_full_name_last_first(self) -> str:
        """Gets the full name in the format LastName FirstName, some cultures show family name first."""

        return f"{self.last_name} {self.first_name}"

    def to_dict(self) -> dict:
        """Converts the object to a dictionary."""

        return {key: vars(self)[key] for key in self.keys()}

    def keys(self) -> [str]:
        """Gets all the keys for the object."""

        return list(vars(self))

    def to_person(self):
        """Create a Person object from the data."""

        person = Person()
        for key in Person().keys():
            person.set(key, self.get(key))

        return person

    def from_record(self, rec: record):
        """Populates person data with data from record."""

        for key in Person().keys():
            self.set(key, rec[key])
