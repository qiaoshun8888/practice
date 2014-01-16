#coding=utf-8
"""
quick sort algorithm:
O(logn) time complexity
should sort the list in place
"""

def quick_sort(unsorted):
	def partition_inplace(unsorted, start, end):
		if (end - start) <= 1:
			return
		elif (end - start) == 2:
			if unsorted[0] > unsorted[1]:
				unsorted[start], unsorted[end] = unsorted[end], unsorted[start]
		pivot = unsorted[-1]
		left_index = start
		right_index = end - 1
		while left_index < right_index:
			if unsorted[left_index] > pivot and  unsorted[right_index] <= pivot:
				unsorted[left_index], unsorted[right_index] = unsorted[right_index], unsorted[left_index]
			elif unsorted[left_index] <= pivot:
				left_index += 1
			elif unsorted[right_index] > pivot:
				right_index -= 1
		unsorted[-1], unsorted[right_index] = unsorted[right_index], unsorted[-1]
		if right_index-1 > start:
			partition_inplace(unsorted, start, right_index-1)
		if right_index+1 < end:
			partition_inplace(unsorted, right_index+1, end)

	partition_inplace(unsorted, 0, len(unsorted)-1 )


if __name__ == '__main__':
	unsorted = [9,8,7,6,5,4,3,2,1,0]
	print unsorted
	quick_sort(unsorted)
	print unsorted

				
