from math import sqrt
a = float(input("enter a : "))
b = float(input("enter b : "))
c = float(input("enter c : "))

s =  (b ** 2)- 4*a*c
r = sqrt(s)

sol1 = (-b + r)/2*a
sol2 = (-b - r)/2*a

print(f"solutions are {sol1} and {sol2}")