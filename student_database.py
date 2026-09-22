# Initialize an empty Dictionary to store student records
student_db = {}

# Helper function to find a student's Roll Number by Name or Roll No
def get_roll_number(action_name):
    print("\n--- " + action_name + " Student ---")
    print("Find student by (1) Roll No or (2) Name?")
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        roll_no = int(input("Enter Roll Number: "))
        return roll_no
        
    elif choice == '2':
        search_name = input("Enter Student Name: ").lower()
        
        # Search for all students matching the name using a standard loop
        matches = []
        for roll in student_db:
            # student_db[roll] is a tuple: (name, branch, marks)
            if student_db[roll][0].lower() == search_name:
                matches.append(roll)
        
        if len(matches) == 0:
            print("Error: No student found with that name.")
            return -1
        elif len(matches) == 1:
            return matches[0]
        else:
            print("\nMultiple students found with that name:")
            for roll in matches:
                branch = student_db[roll][1]
                print(" - Roll No:", roll, "| Branch:", branch)
                
            print("To ensure the correct record is modified, please provide the Roll No.")
            roll_no = int(input("Enter specific Roll Number from the list above: "))
            return roll_no
    else:
        print("Error: Invalid choice.")
        return -1

# 1. Add a new student record
def add_student():
    print("\n--- Add New Student ---")
    roll_no = int(input("Enter Roll Number: "))
    
    if roll_no in student_db:
        print("Error: Roll No already exists.")
    else:
        name = input("Enter Student Name: ")
        branch = input("Enter Branch: ")
        marks_input = input("Enter Marks separated by spaces (e.g., 85 90 92): ")
        
        # Beginner way to convert string to a list of integers
        marks_list_strings = marks_input.split()
        marks = []
        for m in marks_list_strings:
            marks.append(int(m))
            
        # Storing data as a Tuple containing (Name, Branch, List of Marks)
        student_db[roll_no] = (name, branch, marks)
        print("Success: Added record for", name)

# 2. Update an existing student record
def update_student():
    roll_no = get_roll_number("Update")
    
    # -1 means the search failed or was cancelled
    if roll_no == -1:
        return
        
    if roll_no not in student_db:
        print("Error: Roll No not found in database.")
    else:
        # Extract current data
        current_name = student_db[roll_no][0]
        current_branch = student_db[roll_no][1]
        current_marks = student_db[roll_no][2]
        
        print("\nUpdating details (Press Enter without typing anything to keep current values)")
        new_name = input("Enter new Name [" + current_name + "]: ")
        new_branch = input("Enter new Branch [" + current_branch + "]: ")
        new_marks_input = input("Enter new Marks [" + str(current_marks) + "] (space separated): ")
        
        # Check if the user typed something or just pressed Enter
        if new_name == "":
            updated_name = current_name
        else:
            updated_name = new_name
            
        if new_branch == "":
            updated_branch = current_branch
        else:
            updated_branch = new_branch
            
        if new_marks_input == "":
            updated_marks = current_marks
        else:
            marks_list_strings = new_marks_input.split()
            updated_marks = []
            for m in marks_list_strings:
                updated_marks.append(int(m))
                
        # Save the updated Tuple back to the Dictionary
        student_db[roll_no] = (updated_name, updated_branch, updated_marks)
        print("Success: Updated record for Roll No", roll_no)

# 3. Delete an existing student record
def delete_student():
    roll_no = get_roll_number("Delete")
    
    if roll_no == -1:
        return
        
    if roll_no in student_db:
        # Pop removes the item and returns it
        deleted_data = student_db.pop(roll_no)
        print("Success: Deleted record for", deleted_data[0])
    else:
        print("Error: Roll No not found.")

# 4. Display the final student records
def display_records():
    print("\n--- Current Student Records ---")
    if len(student_db) == 0:
        print("No records found.")
    else:
        for roll_no in student_db:
            name = student_db[roll_no][0]
            branch = student_db[roll_no][1]
            marks = student_db[roll_no][2]
            print("Roll No:", roll_no, "| Name:", name, "| Branch:", branch, "| Marks:", marks)
    print("-------------------------------")


# --- Main Menu Loop --

# Pre-loading some data to test the program easily
student_db[101] = ("Aisha Khan", "Computer Science", [85, 90, 92])
student_db[102] = ("John Doe", "Mechanical", [70, 75, 68])
student_db[103] = ("John Doe", "Electrical", [88, 84, 91]) 

while True:
    print("\n=== STUDENT MANAGEMENT SYSTEM ===")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display All Records")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        add_student()
    elif choice == '2':
        update_student()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        display_records()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please select 1-5.")
