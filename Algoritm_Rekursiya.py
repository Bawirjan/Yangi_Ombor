
#   Binary Search  Algoritmi

def binary_search(list, item):
	low = 0
	high = len(list)-1
	while low <= high:
		mid = (low + high)//2
		guess = list[mid]
		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None 

myList1 = [1,2,3,4,5,8,9,12,14,18]
print(binary_search(myList1,5))
# myList1 dan 5 raqamini izlap topib uni indexsini qaytaradi
