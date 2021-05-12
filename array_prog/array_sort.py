n = int(input("enter number of elements : "))


arr = []

for i in range(n):
	k = int(input("enter element : "))
	arr.append(k)
temp = 0

for i in range(n):
	for j in range(i+1,n):
		if arr[i] > arr[j]:
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp

def arrayDisplay(arr,n):
	print("\nsorted array : ",end="")
	for i in range(n):
		print(f"{arr[i]}",end=' ')

arrayDisplay(arr,n)