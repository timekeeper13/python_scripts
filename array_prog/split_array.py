
#split an array and add that it to the end
n = int(input("enter number of elements : "))


arr = []

for i in range(n):
	k = int(input("enter element : "))
	arr.append(k)
s = int(input("enter index to split the array"))

def split(arr,n,s):
	for i in range(s):
		a = arr[0]
		for j in range(n-1):
			arr[j] = arr[j+1]

		arr[n-1] = a

def arrayDisplay(arr,n):
	print("splited array : ",end="")
	for i in range(n):
		print(f"{arr[i]}",end=' ')

split(arr,n,s)
arrayDisplay(arr,n)