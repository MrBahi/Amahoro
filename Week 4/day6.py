print("======== EXERCISE 1: FILE WRITING ==========")
# Write a program that saves your name and city to a text file
# then reads it back and prints it
import tempfile, os
path = tempfile.mktemp(suffix='.txt')
with open(path, 'w') as f:
    f.write("Name: Eric\nCity: Nairobi\n")
with open(path) as f:
    print(f.read())

print("\n========= EXERCISE 2: ERROR HANDLING ==========")
# Wrap a division operation in try/except
# Handle ZeroDivisionError and ValueError separately
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError as e:
        return f"Invalid input: {e}"

print(safe_divide(10, 2))
print(safe_divide(10, 0))

print("\n ========== EXERCISE 3: JSON ==========")
import json
# Create a Python dictionary and convert it to JSON
# Then parse it back and access a value
data = {"name": "Eric", "age": 30, "city": "Nairobi"}
json_str = json.dumps(data, indent=2)
print(json_str)
parsed = json.loads(json_str)
print(f"Name: {parsed['name']}")

print("\n ========= EXERCISE 4: CHALLENGE =========")
import json, tempfile
# Save a list of 3 students (name, score) to JSON
# Read it back and print only students who scored above 70
students = [
    {"name": "Eric", "score": 85},
    {"name": "James", "score": 62},
    {"name": "Amina", "score": 91}
]
path = tempfile.mktemp(suffix='.json')
with open(path, 'w') as f:
    json.dump(students, f)
with open(path) as f:
    loaded = json.load(f)
for s in loaded:
    if s['score'] > 70:
        print(f"{s['name']}: {s['score']}")

print("\n ========= EXERCISE 5: Trade Application — Carpentry Workshop Log")
import io

# Carpentry workshop daily log: day, chairs made, timber used (metres)
workshop_log = """Monday,8,24
Tuesday,6,18
Wednesday,10,30
Thursday,7,21
Friday,9,27
"""

total_chairs = 0
total_timber = 0
days = 0

f = io.StringIO(workshop_log)
for line in f:
    line = line.strip()
    if line:
        day, chairs, timber = line.split(",")
        chairs = int(chairs)
        timber = int(timber)
        print(f"{day}: {chairs} chairs | {timber}m timber")
        total_chairs += chairs
        total_timber += timber
        days += 1

print(f"\nTotal chairs made: {total_chairs}")
print(f"Total timber used: {total_timber}m")
print(f"Average chairs per day: {total_chairs // days}")

print("\n ========= Exercise 6: Farming Application — Dairy Cow Milk Log ==========")
import io

# Dairy log: cow_name, morning_litres, evening_litres
milk_log = """Daisy,6.5,7.2
Bella,4.1,4.8
Nala,8.3,9.1
Rosa,3.2,3.5
Lola,7.8,8.4
"""

total_herd = 0
low_producers = []

f = io.StringIO(milk_log)
for line in f:
    line = line.strip()
    if line:
        name, morning, evening = line.split(",")
        daily = float(morning) + float(evening)
        status = "OK" if daily >= 10 else "LOW"
        print(f"{name}: {daily:.1f} litres [{status}]")
        total_herd += daily
        if daily < 10:
            low_producers.append(name)

print(f"\nHerd total: {total_herd:.1f} litres")
print(f"Low producers: {', '.join(low_producers) if low_producers else 'None'}")

print("\n********* CODED CHALLENGE ************")
volume_data = [ "two hundred" ]
for item in volume_data:
    try:
        volume = int(item)
        if volume >= 220:
            print(volume, "- Goal hit")
        else:
            print(volume,"- Not enough")
    except ValueError:
        print(f"Invalid entry: two hundred is not a number")