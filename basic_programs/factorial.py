
def factorial(n):
	fact = 1
	if n < 0:
		return 0

	elif n == 0:
		return fact
	else:

		for i in range(1,n+1):
			fact = fact*i
		return fact

print(f"factorial : {factorial(10)}")