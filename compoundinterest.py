def comp(p,r,t):
	if t<=0:
		return p
	else:
		return comp((p+(p*r/100)),r,t-1)
p=int(input("enter principle amount"))
r=int(input("enter rate"))
t=int(input("enter years"))
x=comp(p,r,t)
print(x)

