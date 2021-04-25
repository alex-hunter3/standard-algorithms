import random

def insertion_sort(arr):
	for i in range(1, len(arr)):
		temp = arr[i]

		while i > 0 and arr[i - 1] > temp:
			arr[i], arr[i - 1] = arr[i - 1], arr[i]
			i -= 1

	return arr

if __name__ == "__main__":
	arr = []
	
	for i in range(10):
		arr.append(random.randint(1, 20))

	print(arr)
	print(insertion_sort(arr))