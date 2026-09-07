print("========== CODE CHALLENGE: SOCIAL MEDIA API")
data = {
    "user": "Amerix",
    "followers": 1200000,
    "last_post": {
        "title": "Cold shower protocol",
        "likes": 4800
    }
}
# Extract values into clean variables
follower_count = data["followers"]
post_likes = data["last_post"]["likes"]
# Print results
print(f"Followers: {follower_count:}")
print(f"Last post likes: {post_likes:}")

print("\n ============ SUPPLIER CAHLLENGE API =============")
data = {
    "supplier": "Nairobi Steel Ltd",
    "prices": {
        "mild_steel_sheet": 4500,
        "angle_iron": 2800
    }
}
# 1. Look up individual item unit prices from the nested data
sheet_unit_price = data["prices"]["mild_steel_sheet"]
angle_unit_price = data["prices"]["angle_iron"]

# 2. Calculate individual totals based on required quantities
total_sheets_cost = sheet_unit_price * 3
total_angle_cost = angle_unit_price * 6

# 3. Calculate global grand total
grand_total = total_sheets_cost + total_angle_cost

# 4. Print a clean invoice layout with comma-separated currency values
print(f"Mild steel sheets (3): KES{total_sheets_cost:>6}")
print(f"Angle iron (6m): KES{total_angle_cost:>6}")
print(f"Total: KES{grand_total:>6}")

print("\n ============= BOLT DRIVER EARNINGS ===========")
# 1. Initialize counter and tracking trackers
total_fare = 0
highest_fare = 0
highest_route = ""

# 2. Extract the trips array from the primary dictionary mapping block
trips_list = data["trips"]
trip_count = len(trips_list)

# 3. Loop through every trip row entry item
for trip in trips_list:
    current_fare = trip["fare_kes"]
    total_fare += current_fare
    
    # Check if this trip beats the current maximum record value
    if current_fare > highest_fare:
        highest_fare = current_fare
        highest_route = trip["route"]

# 4. Print out the driver dashboard overview invoice
print(f"Driver Name  : {data['driver']}")
print(f"Date         : {data['date']}")
print("=" * 45)
print(f"Total Trips Completed : {trip_count}")
print(f"Total Daily Earnings  : KSh {total_fare:,}")
print(f"Highest Paying Trip   : KSh {highest_fare:,} ({highest_route})")
print("=" * 45)