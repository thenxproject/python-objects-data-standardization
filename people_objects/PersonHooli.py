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

    def to_person(self) -> Person:
        """Returns a Person object using only the data from the person super class."""
        return super()._to_person()
