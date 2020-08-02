import math
def get_digit(num, pos):
	return (abs(num) // (10 ** pos)) % 10

def get_len(num):
	if num == 0:
		return 1
	return math.floor(math.log10(abs(num)) + 1

def get_max(arr):
	max_len = 0
	for num in arr:
		max_len = max(max_len, get_len(num))
	return max_len

def flatten(arr):
	res = []
	for num in arr:
		if isinstance(num, list):
			res.extend(flatten(num))
		else:
			res.append(num)
	return res

def radix_sort(arr):
	max_len = get_max(arr)
	for i in range(max_len):
		buckets = [[] for _ in range(10)]
		for num in arr:
			digit = get_digit(num, i)
			buckets[digit].append(num)
		arr = flatten(buckets)
	return arr
