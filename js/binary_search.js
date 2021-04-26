function binarySearch(arr, target) {
	let top = arr.length - 1;
	let bottom = 0;
	let mid;

	while (bottom <= top) {
		mid = Math.floor((top + bottom) / 2);

		if (arr[mid] === target) return mid;
		else if (arr[mid] > target) top = mid - 1;
		else bottom = mid + 1;
	}

	return -1;
}

const arr = [1, 2, 3, 4, 5, 6];
const target1 = 5;
const target2 = 9;

console.log(binarySearch(arr, target1));
console.log(binarySearch(arr, target2));