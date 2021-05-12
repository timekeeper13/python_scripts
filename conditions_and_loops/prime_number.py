
n = int(input("enter the number : "))

if n > 2 :

	for i in range(2,n):
		if n % i == 0:
			print(f"{n} is not a prime number")
			break;

	else:
		print(f"{n} is a prime number")
			
else:			
	print(f"{n} is not a prime number")