print("========= BASIC GROUPBY ==========")
import pip
import pandas as pd

df = pd.DataFrame({
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

# Average steps per fasting protocol
grouped = df.groupby("protocol")["steps"].mean().round(0)
print("Average steps by protocol:")
print(grouped)

print()
# Total steps per protocol
totals = df.groupby("protocol")["steps"].sum()
print("Total steps by protocol:")
print(totals)

print("\n =========== MULTIPLE AGGREGATIONS =============")
import pip
import pandas as pd

df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian", "Kevin", "James", "Sandra"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa", "Nairobi", "Mombasa"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800, 9800, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 7.0, 8.5],
})

# Multiple aggregations on steps by city
city_stats = df.groupby("city")["steps"].agg(["mean", "max", "min", "count"]).round(0)
print("Steps statistics by city:")
print(city_stats)

print("\n ======== GROUP MULTIPLE COLUMNS ===========")
import pip
import pandas as pd

df = pd.DataFrame({
    "city":     ["Nairobi", "Nairobi", "Mombasa", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Kisumu"],
    "protocol": ["OMAD",    "2MAD",    "OMAD",    "2MAD",    "OMAD",    "OMAD",   "2MAD",    "2MAD"],
    "steps":    [9200, 10500, 8100, 11000, 9400, 10200, 7400, 8800],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 7.5, 8.0, 9.0, 7.5],
})

# Average steps grouped by both city and protocol
breakdown = df.groupby(["city", "protocol"])["steps"].mean().round(0)
print("Average steps by city and protocol:")
print(breakdown)

print("\n ========== VALUE COUNTS ===========")
import pip
import pandas as pd

df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian", "Kevin", "James", "Grace", "Sandra", "James"],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD", "OMAD", "2MAD", "OMAD"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa", "Nairobi", "Kisumu", "Mombasa", "Nairobi"],
})

print("Protocol distribution:")
print(df["protocol"].value_counts())

print("\nCity distribution:")
print(df["city"].value_counts())

print("\n ========= HANDLING MISSING DATA ============")
import pip
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian"],
    "steps":    [9200, None, 8100, 11000, None],
    "sleep_hr": [7.5, 8.0, None, 7.0, 9.0],
})

print("Original with NaN:")
print(df.to_string())

print("\nRows with any missing value:")
print(df[df.isna().any(axis=1)].to_string())

# Fill missing steps with the column mean
df["steps"] = df["steps"].fillna(df["steps"].mean())
df["sleep_hr"] = df["sleep_hr"].fillna(df["sleep_hr"].median())

print("\nAfter filling NaN:")
print(df.to_string())

print("\n ========== Workshop Groupby: Revenue by Material ============")
import pip
import pandas as pd

df = pd.DataFrame({
    "client":   ["Wanjiru", "Otieno", "Kamau", "Mwangi", "Njeri",  "Odhiambo", "Achieng", "Bett"],
    "item":     ["gate",    "grills", "frame", "gate",   "grills", "tank stand","frame",   "gate"],
    "material": ["mild steel","angle iron","hollow tube","mild steel","angle iron","mild steel","hollow tube","mild steel"],
    "price_kes":[28000, 14500, 9800, 32000, 12000, 18500, 11000, 29500],
    "status":   ["paid","paid","pending","paid","paid","pending","paid","paid"],
    "region":   ["Nairobi", "Kiambu", "Machakos", "Nairobi", "Kiambu", "Machakos", "Nairobi", "Kiambu"]
})

print("Revenue by material type:")
by_material = df.groupby("material")["price_kes"].agg(["sum","mean","count"]).round(0)
by_material.columns = ["total_kes", "avg_kes", "jobs"]
print(by_material.sort_values("total_kes", ascending=False).to_string())

print("\nPaid vs pending jobs:")
print(df["status"].value_counts())

print("\nAverage job value by status:")
print(df.groupby("status")["price_kes"].mean().round(0))

region_material = df.groupby(["region", "material"])["price_kes"].agg(["sum", "mean", "count"]).round(0)
region_material.columns = ["total_revenue", "avg_per_job", "job_count"]

# Sort by highest revenue totals first to see who earns the most
region_material = region_material.sort_values("total_revenue", ascending=False)

print("Regional Breakdown (Sorted by Highest Earnings First):")
print(region_material.to_string())