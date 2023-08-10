import pandas as pd
from people_objects.Person import Person
from people_objects.PersonHooli import PersonHooli

data = pd.read_excel(io="data_files/AllFiles.xlsx",
                     sheet_name=None,
                     header=0)
person_a = []
for p in data["CompanyA"].to_records():
    person = Person()
    person.first_name = p["FirstName"]
    person.last_name = p["LastName"]
    person_a.append(person)

hooli_emp = []
for emp in data["Hooli"].fillna("").to_records():
    employee = PersonHooli(emp["FirstName"],
                           emp["LastName"],
                           emp["Line1"],
                           emp["Line2"],
                           emp["City"],
                           emp["State"],
                           emp["Zip"],
                           emp["Phone"],
                           emp["EmailAddress"],
                           emp["Title"],
                           emp["Department"],
                           emp["Salary"],
                           emp["CurrentEmployee"]
                           )
    hooli_emp.append(employee)

print("Hooli dict print")
for e in hooli_emp:
    print(e.to_dict())

print("Hooli cast to Person print dict")
for e in hooli_emp:

    print(e.to_person().to_dict())
    print(e.get_formatted_phone())
