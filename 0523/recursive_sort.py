def bubbleSort(array):
    count = 0
    for idx in range(len(array)-1):
        if array[idx] > array[idx + 1]:
            array[idx],array[idx + 1] = array[idx + 1],array[idx]
            count += 1
    if count == 0:
        return array
    else:       
        return bubbleSort(array)

def swap(A, i, j):
	temp = A[i]
	A[i] = A[j]
	A[j] = temp


def selectionSort(A, i, n):
	min = i
	for j in range(i + 1, n):
		if A[j] < A[min]:
			min = j			# update the index of minimum element
	# swap the minimum element in sublist `A[i…n-1]` with `A[i]`
	swap(A, min, i)
	if i + 1 < n:
		selectionSort(A, i + 1, n)

arr1 = [1,5,2,7,3]
arr2 = [1,5,2,7,3]
selectionSort(arr1, 0, len(arr1))
print("selective sort :{}".format(arr1))
print("bubble sort :{}".format(bubbleSort(arr2)))