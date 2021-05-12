
a = input("first variable")
b = input("second variable")

def swap_temp(a,b):
	temp = a
	a=b
	b=temp
	print("a is {} and b is {}".format(a,b))

swap_temp(a,b)
