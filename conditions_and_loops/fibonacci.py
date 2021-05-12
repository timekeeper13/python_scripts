
a = int(input("enter the number : "))
n=0
s=1
c=1
if s <= 0:
	print("enter postive number")
elif s == 0:
	print("sequence : {n}")
else:
	print("sequence : ",end = (""))
	while c<a:
		print(f"{n},",end=(" "))
		k=n+s
		n=s
		s=k
		c=c+1
	print(n)