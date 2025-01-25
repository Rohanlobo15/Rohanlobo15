arr = [5, 1, 3]

def mergesort(s, e):
    # Base case: If single element, return it as a list
    if s == e:
        return [arr[s]]
    
    mid = (s + e) // 2  # Correctly calculate the middle index
    left = mergesort(s, mid)  # Recursively sort the left half
    right = mergesort(mid + 1, e)  # Recursively sort the right half

    l = []  # To store the merged result
    i, j = 0, 0

    # Merge the two sorted halves
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    # Append remaining elements from `left` (if any)
    while i < len(left):
        l.append(left[i])
        i += 1

    # Append remaining elements from `right` (if any)
    while j < len(right):
        l.append(right[j])
        j += 1

    return l

# Call the function and print the sorted array
print(mergesort(0, len(arr) - 1))
