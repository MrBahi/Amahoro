def get_status(steps):
    if steps > 10000:
        return "Exceeded"
    if steps >= 8000:
        return "Hit"
    return "Missed"

    result1 = get_status(12000)
    result2 = get_status(9000)
    result3 = get_status(5000)

    print(f"12000 steps status: {result1}")
    print(f"9000 steps status: {result2}")
    print(f"5000 steps status: {result3}")

def day_report(steps, water, protocol):
    print("--- Daily Report ---")
    print(f"Steps    : {steps}")
    print(f"Water    : {water} glasses")
    print(f"Protocol : {protocol}")
    print()

def hit_goal(steps):
    return steps >= 8000

day_report(9200, 8, "OMAD")
day_report(7500, 6, "2MAD")
day_report(11000, 9, "Autophagy Marathon")

print("Goal hit (9200)?", hit_goal(9200))
print("Goal hit (7500)?", hit_goal(7500))