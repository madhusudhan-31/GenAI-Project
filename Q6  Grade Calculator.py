# Grade Calculator Program

# Taking marks input
m1 = float(input("Enter marks for Subject 1: "))
m2 = float(input("Enter marks for Subject 2: "))
m3 = float(input("Enter marks for Subject 3: "))
m4 = float(input("Enter marks for Subject 4: "))
m5 = float(input("Enter marks for Subject 5: "))

# Display marks
print("\nMarks Entered:")
print("Subject 1:", m1)
print("Subject 2:", m2)
print("Subject 3:", m3)
print("Subject 4:", m4)
print("Subject 5:", m5)

# Calculations
total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

# Grade Calculation
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Result (All subjects must be >= 40)
if m1 >= 40 and m2 >= 40 and m3 >= 40 and m4 >= 40 and m5 >= 40:
    result = "PASS"
else:
    result = "FAIL"

# Display results
print("\n=== RESULT ===")
print("Total Marks (out of 500):", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)