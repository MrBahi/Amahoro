fruits = ["mango", "banana", "apple", "orange", "grape"]
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.append("pawpaw")
print(fruits)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)

# create a dictionary
student = {
    "name": "Joshua",
    "age": 25,
    "grade": "A"
}
for key, value in student.items():
    print(f"\n{key}: {value}")

# list of 3 dictionaries
students = [
    {"name": "Joshua", "grade": "A"},
    {"name": " Enock", "grade": "B"},
    {"name": " Jonathan", "grade": "C"}
]
for s in students:
    print(f"\n{s['name']}: {s['grade']}")

# Build a simple phonebook
phonebook = {
    "Joshua": "07123456789", 
    "Enock": "07234567890", 
    "Jonathan": "07345678901"
    }
print("=== CONTACTS ====")
for name, number in phonebook.items():
    print(f"\n{name}: {number}")