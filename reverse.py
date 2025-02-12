def reverse_list(lst):
    return [lst[i] for i in range(len(lst) - 1, - 1, - 1)]

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(f"Reversed list: {reverse_list(numbers)} Original list: {numbers}")