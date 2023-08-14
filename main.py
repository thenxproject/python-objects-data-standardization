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

hooli_emp2 = []
for emp in data["Hooli"].fillna("").to_records():
    he2 = PersonHooli()
    he2.from_record(emp)
    hooli_emp2.append(he2)

quarks_bar = []
for c in data["Quarks Bar"].fillna("").to_records():
    cust = Person()
    cust.from_record(c)
    cust.set("tab", float(c["tab"]))
    quarks_bar.append(cust)

print("Hooli dict print")
for e in hooli_emp:
    print(e.to_dict())

print("Hooli 2 dict print")
for e in hooli_emp2:
    print(e.to_dict())

print("Hooli cast to Person print dict")
for e in hooli_emp:

    print(e.to_person().to_dict())
    print(e.get_formatted_phone())

print("Bar tabs")
for c in quarks_bar:
    Person().to_dict()
    print(c.to_dict())

qb_dict = [d.to_dict() for d in quarks_bar]
bar_df = pd.DataFrame.from_records(qb_dict)
print(bar_df)

print("combine lists")
cl = [c.to_person() for c in quarks_bar] + [e.to_person() for e in hooli_emp]
for p in cl:
    print(p.to_dict())
