steps = [8800, 6500, 11000, 9200, 7300]
steps.append(10500)
steps.remove(6500)
steps.sort(reverse=True)
print("Final list:", steps)
# count days over 9000
high_days = 0
for steps in steps:
    if steps >= 9000:
        high_days +=1
print("Days over 9000 steps", high_days)

