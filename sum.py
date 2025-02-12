def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

number = int(input("Enter a number: "))
print(f"sum of digits: {sum_of_digits(number)}")