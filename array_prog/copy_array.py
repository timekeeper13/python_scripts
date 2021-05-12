#copy an array to another
n = int(input("enter number of elements : "))


arr = []

for i in range(n):
	k = int(input("enter element : "))
	arr.append(k)

arr2 = [None]*n

def copy_array(arr,arr2,n):
	for i in range(n):
		arr2[i] = arr[i]

def arrayDisplay(arr,n):
	for i in range(n):
		print(f"{arr[i]}",end=' ')
	print("")

copy_array(arr,arr2,n)
print("array 1 : ",end="")
arrayDisplay(arr,n)

print("array 2 : ",end="")
arrayDisplay(arr2,n)