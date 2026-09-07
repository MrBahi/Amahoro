data = {
    "user": {
        "id": 1,
        "name": "Sandra Weru",
        "city": "Nairobi"
    },
    "metrics": {
        "steps": 10500,
        "sleep_hours": 8.0,
        "bench_press_kg": 80
    },
    "skills": ["welding", "tiling", "copywriting"]
}

print(data["user"]["name"])
print(data["user"]["city"])
print(data["metrics"]["steps"])
print(data["metrics"]["bench_press_kg"], "kg bench press")
print("Skills:", data["skills"])
print("First skill:", data["skills"][0])

print("\n ============= FILTERING API RESULTS ===========")
logs = [
    {"name": "James Omondi",  "steps": 9200,  "protocol": "OMAD"},
    {"name": "Sandra Weru",   "steps": 10500, "protocol": "2MAD"},
    {"name": "Patrick Njiru", "steps": 8100,  "protocol": "OMAD"},
    {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD"},
    {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD"},
    {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD"},
]

# OMAD users who hit 10,000 steps
goal_hitters = [
    r for r in logs
    if r["protocol"] == "OMAD" and r["steps"] >= 10000
]

print("OMAD users who hit 10k steps:")
for r in goal_hitters:
    print(f"  {r['name']}: {r['steps']} steps")