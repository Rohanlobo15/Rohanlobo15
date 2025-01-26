arr = [8, 1, 5, 10, 2]

def quicksort(low, high):
    if high <= low:
        return

    pivot = arr[low]  # Choose the pivot
    i = low + 1
    j = high

    # Single while loop for partitioning
    while i <= j:
        if arr[i] > pivot and arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
            i += 1
            j -= 1
        if arr[i] <= pivot:
            i += 1
        if arr[j] >= pivot:
            j -= 1

    # Place the pivot in its correct position
    arr[low], arr[j] = arr[j], arr[low]

    # Recursively sort the left and right partitions
    quicksort(low, j - 1)
    quicksort(j + 1, high)

quicksort(0, len(arr) - 1)
print(arr)
