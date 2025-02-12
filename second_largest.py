def second_largest(lst):
    unique_numbers = list(set(lst))
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) >= 1 else None

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
result = second_largest(numbers)
print(f"Second largest number: {result}" if result else "Not enough unique numbers")