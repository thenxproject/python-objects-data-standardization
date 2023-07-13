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
        return re.sub(r"[()\-. ]", "", self.phone_number)

    def get_formatted_phone(self) -> str:
        phone = self.get_unformatted_phone()
        return f"({phone[:3]}) {phone[3:6]}-{phone[6:]}"


