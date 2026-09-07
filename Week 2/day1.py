weeks_steps = [3500, 5900, 8700, 9300, 11400, 12600, 7100, 4980]
for steps in weeks_steps:
    if steps >= 8000:
        print(steps, "- Goal hit")
    elif steps >= 5000:
        print(steps, "- On target")
    else:
        print(steps, "Below minimum")
print("Days tracked:", len(weeks_steps))