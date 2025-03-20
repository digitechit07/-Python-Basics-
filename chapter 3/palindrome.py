def is_palindrome(num):
    original_num = num
    reverse_num = 0

    while num > 0:
        last_digit = num % 10
        reverse_num = (reverse_num * 10 )+ last_digit
        num = num //10
    
    return reverse_num == original_num

num = int(input("Enter a Number : "))

if is_palindrome(num):
     print(f"{num} is a Palindrome Number!")
else:
    print(f"{num} is NOT a Palindrome Number!")
