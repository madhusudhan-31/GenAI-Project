# Movie Ticket Pricing System

# Taking user input
age = int(input("Enter age: "))
day = input("Enter day of week: ").lower()
tickets = int(input("Enter number of tickets: "))

# Age-based pricing
if age < 3:
    price = 0
    category = "Free"
elif 3 <= age <= 12:
    price = 150
    category = "Child"
elif 13 <= age <= 59:
    price = 300
    category = "Adult"
else:
    price = 200
    category = "Senior"

# Calculate base total
base_total = price * tickets

# Day-based discount
if day in ["friday", "saturday", "sunday"]:
    discount = base_total * 0.20
else:
    discount = 0

# Final price calculation
final_total = base_total - discount

# Display results
print("\n=== TICKET BILL ===")
print("Category:", category)
print("Base price per ticket: ₹", price)
print("Number of tickets:", tickets)
print("Base total: ₹", base_total)
print("Discount: ₹", discount)
print("Final amount to pay: ₹", final_total)