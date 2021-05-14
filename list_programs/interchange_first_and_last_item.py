
def swap(ls):
	size = len(ls)

	temp = ls[0]
	ls[0] = ls[size-1]
	ls[size-1] = temp

	return ls

list_new = [1,5,3,7,3,8]

print(swap(list_new))


