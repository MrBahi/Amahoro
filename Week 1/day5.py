daily_steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100]
for day in range(1, 8):
    print("Day", day, "- Step goal: 8,000 steps")
minimum = 5000
total = 0
valid_days = 0
for steps in daily_steps:
     if steps < minimum:
         print(f"Skipping {steps} (below minimum)")
         continue # skip this day, go to next
     total += steps
     valid_days += 1
print(f"Valid days: {valid_days}")
print(f"Total steps (valid days): {total}")
print(f"Average: {total// valid_days}")
# Initialize trackers
streak_count = 0
index = 0
# Check each day consecutively from the start
while index < len(daily_steps) and daily_steps[index] >= 5000:
    streak_count += 1  # Add 1 to the streak
    index += 1        # Move to the next day
print(f"Consecutive streak count: {streak_count}")