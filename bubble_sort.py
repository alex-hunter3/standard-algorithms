import random

def bubble_sort(arr):
	swapped = True

	while swapped:
		swapped = False
		for i in range(len(arr) - 1):
			if arr[i] > arr[i+1]:
				swapped = True
				arr[i], arr[i+1] = arr[i+1], arr[i]

	return arr

if __name__ == "__main__":
	arr = []
	
	for i in range(10):
		arr.append(random.randint(1, 20))

	print(f"Unsorted Array: {arr}")
	print(f"Sorted by Bubble sort: {bubble_sort(arr)}")