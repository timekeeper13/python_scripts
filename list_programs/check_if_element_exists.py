
n = int(input("enter the element to check : "))

lists=[1,2,3,4,5,6]

t = 0
for i in lists:
	if n == i:
		print(f"{n} found at index {t}")

	t = t+1
