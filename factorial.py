def factorial(n):
	if n==1:
		return n
	else:
		return (n*factorial(n-1))
n=int(input("enter the number to find factorial"))
x=factorial(n)
print(x)
