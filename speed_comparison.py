from random import randint
from time import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from merge_sort import merge, merge_sort


def makearr(length=5, maxint=50):
    return [randint(0, maxint) for _ in range(length)]


a = makearr(100000, 100)

t0 = time()
s = insertion_sort(a)
t1 = time()
dif = (t1 - t0)


print(dif)

# for an array of 10000 elements
# bubble_sort        6.21264004707
# selection_sort     2.17107892036
# insertion_sort     3.12578511238
# merge_sort         0.04132604599
# quick_sort
# radix_sort

# for an array of 100000 elements
# bubble_sort
# selection_sort
# insertion_sort
# merge_sort         0.489917039871
# quick_sort
# radix_sort
