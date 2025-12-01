def slist_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

nums = [2, 4, 6, 8, 10]
print("Sum of list items:", slist_sum(nums))