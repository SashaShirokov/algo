def merge(arr1, arr2):
    new_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        new_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        new_arr.append(arr2[j])
        j += 1
    return new_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


# test = [8, 14, 28, 9, -29, -58, 89, 5, 7, -23]
# print(merge_sort(test))


print(merge([2, 5, 8], [1, 3, 8]))
