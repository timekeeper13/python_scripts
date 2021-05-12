#smallest element of an array
n = int(input("enter number of elements : "))


arr = []

for i in range(n):
	k = int(input("enter element : "))
	arr.append(k)

smallest = arr[0]
for i in range(1,n):
	if smallest > arr[i]:
		smallest = arr[i]
print(f"smallest element is {smallest}")