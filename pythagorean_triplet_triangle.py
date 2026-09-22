# Function to check if the triangle is right-angled
def is_right_angled(a, b, c):
    # Calculate the squares of all three sides
    sq_a = a * a
    sq_b = b * b
    sq_c = c * c
    
    # Check all three possibilities for the hypotenuse (longest side)
    if (sq_a + sq_b == sq_c) or (sq_a + sq_c == sq_b) or (sq_b + sq_c == sq_a):
        return True
    else:
        return False

# --- Main Program ---
print("--- Right-Angled Triangle Checker ---")

# Take the three sides as input from the user
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Call the function and use an if/else structure to print the result
if is_right_angled(side1, side2, side3):
    print("\nYes, this is a right-angled triangle.")
else:
    print("\nNo, this is NOT a right-angled triangle.")