daily_log = { 
    "steps": 9200,
    "water_glasses": 7,
    "workout": None,
    "cold_shower": True,
}

print(daily_log)
print("Steps:", daily_log.get("steps"))

my_log = {
    "steps": 11000,
    "water_glasses": 13,
    "fasting_protocol": "2MAD",
    "cold_shower": True,
    "sleep_hours": 7
}
print("My records:")
for key, value in my_log.items():
    print(key, ":", value)
if my_log["steps"] >= 10000:
    print("Steps reached. Today was a great day, you did very well. Indeed, better than yesterday.")