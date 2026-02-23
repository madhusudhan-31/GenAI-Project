# Age Calculator (Basic Version)

# Take birth year input
birth_year = int(input("Enter your birth year: "))

# Current year (change if needed)
current_year = 2026

# Calculate age
age = current_year - birth_year

print("Current Age:", age)
print("Age in months:", age * 12)
print("Age in days (approx):", age * 365)
print("Age in hours (approx):", age * 365 * 24)
print("Age in minutes (approx):", age * 365 * 24 * 60)
print("Years until 100:", 100 - age)