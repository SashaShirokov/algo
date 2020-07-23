def pivot(arr, start):
    pivVal = arr[start]
    pivInd = start
    for i in range(start + 1, len(arr)):
        if arr[i] < pivVal:
            pivInd += 1
            arr[i], arr[pivInd] = arr[pivInd], arr[i]
    arr[start], arr[pivInd] = arr[pivInd], arr[start]
    return pivInd


def quick_sort(arr, start=0, end=None):
    if end == None:
        end = len(arr)
    print('test: ', arr)
    if start < end:

        pivVal = pivot(arr, start)
        quick_sort(arr, start, pivVal - 1)  # -1 is under question
        quick_sort(arr, pivVal + 1, end)
    return arr


print(quick_sort([4, 6, 9, 1, 2, 5, 3]))
