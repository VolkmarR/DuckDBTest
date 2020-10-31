import csv
from faker import Faker

# init
countPersons = 100
countBooks = 100
countOrderItems = 1000

fake = Faker()

# create persons csv

with open('testData\\persons.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "name", "street", "city", "email"])
    for id in range(1, countPersons + 1):
        writer.writerow([id, fake.name(), fake.street_address(), fake.city(), fake.email()])

with open('testData\\books.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "isbn", "name", "category", "price"])
    for id in range(1, countBooks + 1):
        writer.writerow([id, fake.isbn13(), fake.catch_phrase(), fake.random_int(1, 10), fake.random_int(1000, 7500)  / 100])

with open('testData\\orderItems.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "person_id", "book_id", "quantity", "date"])
    for id in range(1, countOrderItems + 1):
        writer.writerow([id, fake.random_int(1, countPersons), fake.random_int(1, countBooks), fake.random_int(1, 5), fake.date_this_year()])
