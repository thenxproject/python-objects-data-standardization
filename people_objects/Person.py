import re


class Person:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.street_address = ""
        self.unit = ""
        self.city = ""
        self.state = ""
        self.zip_code = ""
        self.phone_number = ""
        self.email = ""

    def get_unformatted_phone(self) -> str:
        """Does a regex substitution to replace formatting characters."""
        return re.sub(r"[()\-. ]", "", self.phone_number)

    def get_formatted_phone(self) -> str:
        """Gets a phone number formatted as (###) ###-####."""
        phone = self.get_unformatted_phone()
        return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"

    def get_full_name(self) -> str:
        """Gets the full name in the format FirstName LastName."""
        return f"{self.first_name} {self.last_name}"

    def get_full_name_last_first(self) -> str:
        """Gets the full name in the format LastName FirstName, some cultures show family name first."""
        return f"{self.last_name} {self.first_name}"


