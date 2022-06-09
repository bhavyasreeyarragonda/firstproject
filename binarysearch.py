def binary_search(my_list, low, high, x):
	if high >= low:
		mid = (high + low) // 2
		if my_list[mid] == x:
			return mid
		elif my_list[mid] > x:
			return binary_search(my_list, low, mid - 1, x)
		else:
			return binary_search(my_list, mid + 1, high, x)
	else:
		return -1
my_list = [ 1, 2,3,4 ]
x= int(input("enter the element to search"))
my_result = binary_search(my_list,0,len(my_list)-1,x)
if my_result != -1:
	print("Element found at index ", str(my_result))
else:
	print("Element not found!")
