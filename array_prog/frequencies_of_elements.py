n = int(input("enter number of elements : "))
#number of occurance of each elements in an array

arr = []

for i in range(n):
	k = int(input("enter element : "))
	arr.append(k)


arr2 = [None]*n


for i in range(n):
	count = 1
	for j in range(i+1,n):
		if arr[i] == arr[j]:
			count = count + 1
			arr2[j] = "visited"
	
	if arr2[i] != "visited":
		arr2[i] = count


print("element | count")
for i in range(n):
	if arr2[i] != "visited":
		print(f"--   {arr[i]} \t| {arr2[i]}   --")