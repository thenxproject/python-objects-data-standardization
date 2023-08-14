from openpyxl.pivot import record

from people_objects.Person import Person


class PersonHooli(Person):
    def __init__(self,
                 first_name: str = "",
                 last_name: str = "",
                 street_address: str = "",
                 unit: str = "",
                 city: str = "",
                 state: str = "",
                 zip_code: str = "",
                 phone_number: str = "",
                 email: str = "",
                 title: str = "",
                 department: str = "",
                 salary: str = "",
                 current_employee: bool = False
                 ):
        super().__init__(first_name=first_name,
                         last_name=last_name,
                         street_address=street_address,
                         unit=unit,
                         city=city,
                         state=state,
                         zip_code=zip_code,
                         phone_number=phone_number,
                         email=email
                         )
        self.title: str = title
        self.department: str = department
        self.salary: str = salary
        self.current_employee: bool = bool(current_employee)

    __key_map_str = {
        "FirstName": "first_name",
        "LastName": "last_name",
        "EmailAddress": "email",
        "Phone": "phone_number",
        "Line1": "street_address",
        "Line2": "unit",
        "City": "city",
        "State": "state",
        "Zip": "zip_code",
        "Title": "title",
        "Department": "department",
        "Salary": "salary"
    }

    __key_map_bool = {
        "CurrentEmployee": "current_employee"
    }

    def to_person(self) -> Person:
        """Returns a Person object using only the data from the person super class."""

        return super().to_person()

    def from_record(self, rec: record):
        """Populates person data with data from record."""

        for key in self.__key_map_str.keys():
            self.set(self.__key_map_str[key], rec[key])

        for key in self.__key_map_bool.keys():
            self.set(self.__key_map_bool[key], bool(rec[key]))
