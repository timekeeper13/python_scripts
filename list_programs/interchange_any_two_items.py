
f = int(input("enter fisrt index"))
l = int(input("enter second index"))

def swap(ls):
	temp = ls[f]
	ls[f] = ls[l]
	ls[l] = temp

	return ls

list_new = [1,4,6,3,4,8]

print(swap(list_new))