print(" =========== DATAFRAME ===========")
import pip
import pandas as pd

data = {
    "Day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "Steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "Sleep hours": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "Protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "Cold shower": [True, True, False, True, True, True, True]
}

df = pd.DataFrame(data)
print(df.to_string())

print("\n ========= INSPECTING A DATAFRAME =============")
import pip
import pandas as pd

data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "cold_shower": [True, True, False, True, True, True, True]
}
df = pd.DataFrame(data)

print("Shape (rows, cols):", df.shape)
print("\nColumns:", list(df.columns))
print("\nData types:")
print(df.dtypes)
print("\nFirst 3 rows:")
print(df.head(3).to_string())

print("\n =========== SELECTING COLUMNS ==========")
import pip
import pandas as pd

data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
}
df = pd.DataFrame(data)

# Single column (returns a Series)
print("Steps column:")
print(df["steps"])

print("\nSteps and protocol:")
print(df[["steps", "protocol"]].to_string())

print("\n ========== SELECTING ROWS ==========")
import pip
import pandas as pd

data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
}
df = pd.DataFrame(data)

# iloc: by position
print("First row (iloc[0]):")
print(df.iloc[0])

print("\nRows 0 to 2 (iloc[0:3]):")
print(df.iloc[0:3].to_string())

print("\nLast row (iloc[-1]):")
print(df.iloc[-1])

print("\n =========== BASIC STATISTICS WITH DESCRIBE============")
import pip
import pandas as pd

data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8],
    "bench_press_kg": [80, 82, 91, 87, 84, 85, 88],
}
df = pd.DataFrame(data)

print("Statistics for all numeric columns:")
print(df.describe().to_string())

print("\nManual checks:")
print(f"Mean steps:  {df['steps'].mean():.0f}")
print(f"Max steps:   {df['steps'].max()}")
print(f"Min steps:   {df['steps'].min()}")
print(f"Total steps: {df['steps'].sum()}")
print(f"Total Kg: {df['bench_press_kg'].sum()}")

print("\n ========== PRACTICAL EXAMPLE: A CHICKEN FARM WEEKLY LOG ===========")
import pip
import pandas as pd

data = {
    "day":        ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "eggs":       [312, 298, 320, 305, 290, 315, 308],
    "feed_kg":    [18.5, 18.0, 19.2, 18.8, 17.5, 18.6, 19.0],
    "deaths":     [0, 1, 0, 0, 2, 0, 0],
    "pen":        ["A", "A", "A", "B", "B", "B", "A"],
}

df = pd.DataFrame(data)
df["revenue_KES"] = df["eggs"] * 18

print("Weekly egg production log:")
print(df.to_string())

print("\nShape:", df.shape)
print("\nSummary statistics:")
print(df[["eggs", "feed_kg", "deaths"]].describe().round(1).to_string())

weekly_revenue = df["revenue_KES"].sum()
print(f"\nTotal eggs this week:  {df['eggs'].sum()}")
print(f"Average daily eggs:    {df['eggs'].mean():.1f}")
print(f"Worst day (eggs):      {df.loc[df['eggs'].idxmin(), 'day']} ({df['eggs'].min()} eggs)")
print(f"Best day (eggs):       {df.loc[df['eggs'].idxmax(), 'day']} ({df['eggs'].max()} eggs)")

print(f"Total revenue: KES {weekly_revenue:,}")