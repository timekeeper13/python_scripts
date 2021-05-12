
n = int(input("enter the number : "))

sum = 0
for i in range(1,n+1):
	sum = sum + i*i*i

print(f"the cube sum of {n} natural numbers are {sum}")