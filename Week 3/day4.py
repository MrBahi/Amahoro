people = [
    {"name": "James", "steps": [9200, 10500, 8800, 11000, 7600]},
    {"name": "Sandra", "steps": [7000, 7500, 6800, 8000, 7200, 8500, 7800]},
    {"name": "Mwangi", "steps": [10000, 11500, 9800, 12000, 10500, 11000, 10800]},
    {"name": "Patrick", "steps": [8500, 9000, 8800, 9200, 8600, 9400, 9100]}
]
#1. All steps counts above 10,000 across all people
all_steps = [s for p in people for s in p["steps"]]
high_steps = [s for s in all_steps if s > 10000]
print("Steps above 10000:", high_steps)
#2. Names with average steps above 9000
high_avg_names = [p["name"] for p in people if sum(p["steps"]) / len(p["steps"]) > 9000]
print("High average performers:", high_avg_names)