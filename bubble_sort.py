def bubble_sort(arr):
    for i in range(len(arr), 0, -1):
        swapped = False
        for j in range(i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
<<<<<<< HEAD

print('hey man')
>>>>>>> test
a = [8, 10, 38, 17]
print(bubble_sort(a))
