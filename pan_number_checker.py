import re

print("--- PAN Number Validator ---")

# 1. Accept the PAN number from the user
pan_number = input("Enter a PAN number: ")

# 2. Define the regular expression pattern
# Breakdown of the pattern:
# ^        : Starts exactly with what follows
# [A-Z]{5} : Exactly 5 uppercase letters (A through Z)
# [0-9]{4} : Exactly 4 digits (0 through 9)
# [A-Z]    : Exactly 1 uppercase letter
# $        : Ends exactly there (no extra characters allowed)
pattern = "^[A-Z]{5}[0-9]{4}[A-Z]$"

# 3. Check if the input matches the pattern using re.fullmatch()
# fullmatch ensures the ENTIRE string matches the pattern, not just a part of it
if re.fullmatch(pattern, pan_number):
    print("Valid PAN Number")
else:
    print("Invalid PAN Number")