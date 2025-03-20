# Take input from the user
num = int(input("Enter a number: "))

# Store original number for later comparison
original_num = num  

# Initialize sum to 0
armstrong_sum = 0  

# Count digits in the number
num_digits = len(str(num))

# Extract each digit and calculate sum of powers
while num > 0:
    digit = num % 10  # Get last digit
    armstrong_sum += digit ** num_digits  # Raise to power and add to sum
    num = num // 10  # Remove last digit

# Check if Armstrong number
if armstrong_sum == original_num:
    print(f"{original_num} is an Armstrong number ✅")
else:
    print(f"{original_num} is NOT an Armstrong number ❌")
