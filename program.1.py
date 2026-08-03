def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr
numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original List:", numbers)
sorted_numbers = bubble_sort(numbers)
print("Sorted List:", sorted_numbers)