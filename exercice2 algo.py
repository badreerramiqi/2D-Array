# Prompt the user to input the first number
n = int(input("Type the first number: "))
# Prompt the user to input the second number
p = int(input("Type the second number: "))

# Validate input range for n and p (between 0 and 10)
while p < 0 or p > 10 or n < 0 or n > 10:
    # If input is out of range, prompt the user to input again
    n = int(input("Type the first number between 0 and 10: "))
    p = int(input("Type the second number between 0 and 10: "))

# Initialize an empty list to store the 2D array
t = []
# Initialize a variable k to keep track of values to be added to the array
k = 0

# Populate the 2D array 't' with values based on user inputs
for i in range(0, n):
    # Initialize an inner list to represent each row
    l = []
    for j in range(0, p):
        # Increment k and add it to the inner list
        k += 1
        l.append(k)
    # Add the inner list to the main list, creating a 2D array
    t.append(l)

# Print the elements of the 2D array 't'
for i in range(0, n):
    for j in range(0, p):
        print(t[i][j])

# Print the elements of the 2D array 't' with a modified order
for i in range(0, n):
    for j in range(0, p):
        # Print elements in reverse order for odd-numbered rows
        if i % 2 != 0:
            print(t[i][p - 1 - j])
        else:
            # Print elements in normal order for even-numbered rows
            print(t[i][j])
