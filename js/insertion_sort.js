function insertionSort(arr) {
	for (let i = 1; i < arr.length; i++) {
		let temp = arr[i];
		let pos = i - 1;

		while ((pos > -1) && (temp < arr[pos])) {
			arr[pos + 1] = arr[pos];
			pos--;
		}

		arr[pos + 1] = temp;
	}

	return arr;
}

let unsorted = [5, 2, 4, 6, 1, 3];
console.log(unsorted);
console.log(insertionSort(unsorted));