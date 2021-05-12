n = int(input("enter number of elements : "))

arr = []

for i in range(n):
	k = int(input("enter element : "))
	arr.append(k)



def largest(arr,n):
	large = arr[0]
	for i in range(1,n):
		if arr[i] > large:
			large = arr[i]
	return large

s = largest(arr,n)
print(f"\nlargest number is : {s}")
