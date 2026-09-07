import json

# Simulated API response with nested data
api_json = '''
{
  "client": "James Omondi",
  "week": 1,
  "daily_logs": [
    {"day": "Monday",    "steps": 9200,  "protocol": "OMAD"},
    {"day": "Tuesday",   "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800,  "protocol": "OMAD"},
    {"day": "Thursday",  "steps": 11000, "protocol": "Autophagy Marathon"},
    {"day": "Friday",    "steps": 7600,  "protocol": "OMAD"},
    {"day": "Saturday",   "steps": 10400,   "protocol": "Autophagy marathon"}
  ]
}
'''

data = json.loads(api_json)

print("Client:", data["client"])
print("Week:", data["week"])
print()

for log in data["daily_logs"]:
    status = "OK" if log["steps"] >= 8000 else "low"
    print(f"  {log['day']}: {log['steps']} steps ({status})")

print("\n==========EXERCISE===============")
import json

week_report = {
    "name": "James",
    "steps": [9200, 10500, 8800, 11000, 7600],
    "protocols": ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD"]
}

# Convert to JSON
json_str = json.dumps(week_report, indent=2)
print("JSON output:")
print(json_str)

# Load back and calculate average
loaded = json.loads(json_str)
avg = sum(loaded["steps"]) / len(loaded["steps"])
print(f"\nAverage steps for {loaded['name']}: {round(avg)}")