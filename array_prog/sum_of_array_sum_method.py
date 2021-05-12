
n = int(input("enter number of elements : "))

arr = []

for i in range(n):
	k = int(input("enter element : "))
	arr.append(k)

sum =sum(arr)
print(f"\nsum of array is : {sum}")
