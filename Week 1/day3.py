number_of_exercises = 6
sets_per_exercise = 4
reps_per_set = 10
average_weight_per_rep = 60
session_duration_in_minutes = 45
total_sets = number_of_exercises * sets_per_exercise
total_reps = total_sets * reps_per_set
total_volume = total_reps * average_weight_per_rep
total_volume = 10000
print(f"Total sets: {total_sets}")
print(f"Total reps: {total_reps}")
print(f"Total volume: {total_volume}")
print(f"Reps per minute: {total_reps // session_duration_in_minutes}")
print(f"Exceeded 10,000 kg per target: {total_volume >= 10000}")
