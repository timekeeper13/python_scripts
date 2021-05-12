n = int(input("enter number of elements : "))


arr = []

for i in range(n):
	k = int(input("enter element : "))
	arr.append(k)

def rotate(arr,s,e):
	while e>s:
		temp = arr[s]
		arr[s] = arr[e]
		arr[e] = temp

		s = s+1
		e = e-1

def rotation(arr,n):
	rotate(arr,0,n-1)

def arrayDisplay(arr,n):
	print("reverse array : ",end="")
	for i in range(n):
		print(f"{arr[i]}",end=' ')

rotation(arr,n)
arrayDisplay(arr,n)