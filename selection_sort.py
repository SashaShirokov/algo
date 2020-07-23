def sel(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if i != min:
            arr[i], arr[min] = arr[min], arr[i]
    return arr


print(sel([8, 10, 0, 18, 29]))
