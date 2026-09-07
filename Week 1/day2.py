name = "Axel"
steps_walked_today = 9500
hours_of_sleep = 6.5
water_glasses = 12
cold_shower = True
current_skill_being_learned = "python"
steps_as_string = "9500" # this is a str, not a number
steps_as_int = int(steps_as_string) # now it is an int
# you can now do maths with it
target = 10000
gap = target - steps_as_int
print(f"My name is {name}. I slept {hours_of_sleep} hours today. I have drunk {water_glasses} glasses of water and I have taken a {cold_shower} shower. I am learning {current_skill_being_learned} as a skill. I need {gap} more steps to hit my target.")
print(type(steps_as_string))
print(type(steps_as_int))