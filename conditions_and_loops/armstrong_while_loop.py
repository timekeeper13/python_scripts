
n = int(input("enter number : "))

k = 0
t = n

while n>0:
	d = n % 10
	k = k+(d*d*d)
	n=int(n/10)

if t == k:
	print(f"the number {t} is an armstrong number")
else:
	print(f"the number {t} is not an armstrong number")