package main

import "fmt"

// MergeSort sorts an integer slice using the merge sort algorithm.
// Time complexity: O(n log n)
// Space complexity: O(n)
func MergeSort(arr []int) {
	if len(arr) <= 1 {
		return
	}

	mid := len(arr) / 2
	left := make([]int, mid)
	right := make([]int, len(arr)-mid)

	copy(left, arr[:mid])
	copy(right, arr[mid:])

	MergeSort(left)
	MergeSort(right)
	merge(arr, left, right)
}

// merge combines two sorted slices into the original slice.
func merge(arr, left, right []int) {
	i, j, k := 0, 0, 0

	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			arr[k] = left[i]
			i++
		} else {
			arr[k] = right[j]
			j++
		}
		k++
	}

	for i < len(left) {
		arr[k] = left[i]
		i++
		k++
	}

	for j < len(right) {
		arr[k] = right[j]
		j++
		k++
	}
}

func main() {
	arr := []int{38, 27, 43, 3, 9, 82, 10}
	fmt.Println("Original array:", arr)
	MergeSort(arr)
	fmt.Println("Sorted array:", arr)
}