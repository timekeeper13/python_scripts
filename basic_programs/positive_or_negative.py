
def positive_negative(n):
	if n > 0 :
		return "positive"
	elif n == 0:
		return "zero"
	else:
		return "negative"

num = positive_negative(-1)

print(f"the number is {num}")