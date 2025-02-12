def remove_duplicates(lst):
    return list(set(lst))

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(f"List without duplicates: {remove_duplicates(numbers)}")