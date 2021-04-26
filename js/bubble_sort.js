function bubbleSort(arr) {
	let swapped = true;

	while (swapped) {
		swapped = false;

		for (let i = 0; i < arr.length - 1; i++) {
			if (arr[i] > arr[i + 1]){
				[arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
				swapped = true
			}
		}
	}

	return arr;
}

let unsorted = [5, 2, 4, 6, 1, 3];
console.log(unsorted);
console.log(bubbleSort(unsorted));