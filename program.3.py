def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Move elements greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
numbers = [12, 11, 13, 5, 6]

print("Original List:", numbers)
sorted_numbers = insertion_sort(numbers)
print("Sorted List:", sorted_numbers)