from random import randint
from insertion_sort import *

# Returns position in array if found otherwise returns -1
def binary_search(arr, target):
	bottom = 0
	top = len(arr) - 1

	while bottom <= top:
		mid = (top + bottom) // 2

		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			top = mid - 1
		else:
			bottom = mid + 1

	return -1

if __name__ == "__main__":
	arr = []
	target = randint(1, 20)
	
	for i in range(10):
		arr.append(randint(1, 20))

	arr = insertion_sort(arr)

	print(f"Array: {arr}")
	print(f"Target: {target}")
	print(f"Position found: {binary_search(arr, target)}")