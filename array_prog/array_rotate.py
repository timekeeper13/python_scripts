n = int(input("enter number of elements : "))


arr = []

for i in range(n):
	k = int(input("enter element : "))
	arr.append(k)
k = int(input("enter number of rotations : "))
#array rotattion
def rotate(arr,n):
	temp=arr[0]
	for i in range(n-1):
		arr[i]=arr[i+1]
	arr[n-1] = temp

def rotate_all(arr,n,k):
	for i in range(k):
		rotate(arr,n)

def arrayDisplay(arr,n):
	print("rotated array : ",end="")
	for i in range(n):
		print(f"{arr[i]}",end=' ')

rotate_all(arr,n,k)
arrayDisplay(arr,n)
