
def swap(ls):

	f = ls.pop(0)
	l = ls.pop(-1)

	ls.insert(0,l)
	ls.append(f)

	return ls

lsit_new = [2,6,7,3,4,8]

print(swap(lsit_new))
