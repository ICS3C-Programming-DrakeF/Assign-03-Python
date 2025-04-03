# Accept two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the numbers
if num1 > num2:
    print(f"The first number ({num1}) is larger.")
    print(f"The second number ({num2}) is smaller.")
elif num1 < num2:
    print(f"The second number ({num2}) is larger.")
    print(f"The first number ({num1}) is smaller.")
else:
    print("Both numbers are equal.")
