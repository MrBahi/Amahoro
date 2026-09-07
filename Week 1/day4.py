steps = 7500
sleep_hours = 6
water_glasses = 5
cold_shower = False
pages_read = 15
if steps >= 10000:
    print("Steps: Excellent")
elif steps >= 7500:
    print("Steps done: Good")
else:
    print("Steps done: Needs work")
if sleep_hours >= 7:
    print("Sleep hours done: Good")
else:
 print("Sleep hours done: Low")
if water_glasses >= 8:
    print("Glasses of water drunk: Good")
else:
    print("Glasses of water drunk: Low")
if cold_shower:
    print("Cold showe: Completed")
else:
    print("Cold shower: Skipped")
if pages_read >= 10:
    print("Pages read: Good")
else:
    print("Pages read: Below")
# check if all goals are met
if steps >= 7500 and sleep_hours >= 6 and water_glasses >= 5 and cold_shower and pages_read >= 10:
    print("All target goals achieved.")
else:
    print("Some targets missed. Focus on optimizing your physical recovery.")

