# Personal Bio Card Program

# Variables
name = "MadhusudhanGowda H G"
age = 20
course = "Python Programming"
college = "CMRIT"
email = "mahg22cs@cmrit.ac.in"
width = 40
print("╔" + "═" * (width - 2) + "╗")
print("║" + "STUDENT BIO CARD".center(width - 2) + "║")
print("╠" + "═" * (width - 2) + "╣")
print("║ " + f"Name    : {name}".ljust(width - 3) + "║")
print("║ " + f"Age     : {age} years".ljust(width - 3) + "║")
print("║ " + f"Course  : {course}".ljust(width - 3) + "║")
print("║ " + f"College : {college}".ljust(width - 3) + "║")
print("║ " + f"Email   : {email}".ljust(width - 3) + "║")
print("╚" + "═" * (width - 2) + "╝")