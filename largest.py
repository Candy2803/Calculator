def find_largest(numbers):
    return max(numbers)

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(f"Largest number is {find_largest(numbers)}")