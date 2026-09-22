import numpy as np

print("--- Matrix Addition using NumPy ---")
print("Rule: To add two matrices, they MUST have the exact same number of rows and columns.\n")

# 1. Get dimensions for Matrix 1
rows1 = int(input("Enter number of rows for Matrix 1: "))
cols1 = int(input("Enter number of columns for Matrix 1: "))

# 2. Get dimensions for Matrix 2
rows2 = int(input("Enter number of rows for Matrix 2: "))
cols2 = int(input("Enter number of columns for Matrix 2: "))

# 3. Check the mathematical condition for Matrix Addition
if rows1 != rows2 or cols1 != cols2:
    print("\nError: Matrix addition is not possible. The dimensions do not match.")
else:
    print("\nDimensions match! Please enter the data.")
    
    # Helper function to collect matrix data from the user
    def get_matrix_data(matrix_name, rows, cols):
        print("\nEntering data for " + matrix_name + ":")
        matrix_list = []
        
        for i in range(rows):
            print("Enter", cols, "numbers for row", i + 1, "separated by spaces:")
            row_string = input()
            
            # Convert string input to a list of integers using a beginner loop
            row_numbers = []
            for num in row_string.split():
                row_numbers.append(int(num))
                
            matrix_list.append(row_numbers)
            
        # Convert the standard Python nested list into a NumPy array
        return np.array(matrix_list)

    # 4. Get input for both matrices
    matrix1 = get_matrix_data("Matrix 1", rows1, cols1)
    matrix2 = get_matrix_data("Matrix 2", rows2, cols2)

    # 5. Perform matrix addition (Vectorized by NumPy)
    result_matrix = matrix1 + matrix2

    # 6. Display results
    print("\n--- Matrix 1 ---")
    print(matrix1)

    print("\n--- Matrix 2 ---")
    print(matrix2)

    print("\n--- Result of Addition ---")
    print(result_matrix)