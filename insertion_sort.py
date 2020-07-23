def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur_val = arr[i]
        while i > 0 and arr[i - 1] > cur_val:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = cur_val
    return arr


print(insertion_sort([8, 2, 0, -4, 10, 9]))
