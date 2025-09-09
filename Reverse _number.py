number = int(input("Please enter a number: "))
digit_count = 0
temp = number
while temp > 0:
    digit = temp % 10             
    digit_count += 1
    temp //= 10 
    reverse_number=int(str(number)[::-1])                 
print("Number of digits:", digit_count)
print("Reversed number:",reverse_number)
if temp<=0:
    print("Enter a positive number")