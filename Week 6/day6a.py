print(f"Exercise: Patient Risk Screening")
# Paste the data above, then filter df for each condition and print the counts
import pip
import pandas as pd

patients = [
    {"name": "Alice",  "bp": 155, "glucose": 130, "creatinine": 0.9},
    {"name": "Brian",  "bp": 120, "glucose": 118, "creatinine": 1.5},
    {"name": "Carol",  "bp": 148, "glucose": 142, "creatinine": 1.0},
    {"name": "David",  "bp": 130, "glucose": 110, "creatinine": 0.8},
    {"name": "Eve",    "bp": 160, "glucose": 98,  "creatinine": 1.1},
    {"name": "Frank",  "bp": 125, "glucose": 115, "creatinine": 0.7},
]
df = pd.DataFrame(patients)

# 1. CREATE THE COLUMNS FIRST (Move these lines up here!)
df["hypertension_risk"] = df["bp"].apply(lambda x: "Yes" if x > 140 else "No")
df["diabetes_risk"]     = df["glucose"].apply(lambda x: "Yes" if x > 126 else "No")
df["kidney_risk"]       = df["creatinine"].apply(lambda x: "Yes" if x > 1.2 else "No")

# 2. COUNT THE VALUES SECOND (Keep these lines below creation)
ht_count     = df["hypertension_risk"].value_counts().get("Yes", 0)
diab_count   = df["diabetes_risk"].value_counts().get("Yes", 0)
kidney_count = df["kidney_risk"].value_counts().get("Yes", 0)

# 3. PRINT STATEMENTS (Keep these at the very bottom)
print(f"\nHypertension risk: {ht_count}")
print(f"Diabetes risk: {diab_count}")
print(f"Kidney risk: {kidney_count}")
