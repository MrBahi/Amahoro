print("========= GIT COMMANDS =========")
# Git is a terminal tool, not Python.
# Use this terminal to review the logic behind each command.

# Simulate tracking changes
changes = []
changes.append("Created hello.py")
changes.append("Added user input")
changes.append("Fixed loop bug")

for i, msg in enumerate(changes, 1):
    print(f"commit {i}: {msg}")

print("\n========= BRANCHING LOGIC =========")
# Simulate a branching workflow in Python
branches = {"main": ["initial commit", "add README"], "feature": ["add login page"]}

current = "main"
print(f"On branch: {current}")
for commit in branches[current]:
    print(f"  {commit}")

print("\n======== MERGE SIMULATION ========")
# Simulate merging a feature branch into main
branches = {
    "main": ["initial commit", "add README"],
    "feature": ["add login page", "add auth logic"]
}

# Merge feature into main
branches["main"].extend(branches["feature"])
print("After merge, main branch history:")
for commit in branches["main"]:
    print(f"  {commit}")

print("\n========= CHALLENGE =========")
# Write a Python script that generates a README template
# for a GitHub project
project = "AI Text Summariser"
desc = "A Python tool that summarises long text using the OpenAI API."
tech = ["Python", "OpenAI API", "Flask"]

print(f"# {project}")
print(f"\n{desc}\n")
print("## Tech Stack")
for t in tech:
    print(f"- {t}")

print("\n========= TRADE APPLICATION: CARPENTRY PRICING TOOL COMMIT LOG =========")
commits = [
    {"hash": "a1b2c3", "date": "2026-06-01", "message": "Initial commit: basic chair price calculator"},
    {"hash": "d4e5f6", "date": "2026-06-03", "message": "Add timber cost per metre calculation"},
    {"hash": "g7h8i9", "date": "2026-06-05", "message": "Fix rounding error in total material cost"},
    {"hash": "j0k1l2", "date": "2026-06-08", "message": "Add labour cost per day input"},
    {"hash": "m3n4o5", "date": "2026-06-10", "message": "Add profit margin calculator"},
]

print("Commit History: Carpentry Pricing Tool")
print("-" * 50)
for i, c in enumerate(commits, 1):
    print(f"{i}. [{c['hash']}] {c['date']}: {c['message']}")

print(f"\nTotal commits: {len(commits)}")
print(f"Latest: {commits[-1]['message']}")

print("-" * 70)
print("EXERCISE")
commits = [
    "Initial commit",
    "Add SMP tracker script",
    "Fix loop logic in day5.py",
    "Add requirements.txt"
]
for index, message in enumerate(commits, start=1):
    print(f"{index}. {message}")
