s=input("enter the string:")
s1=input("enter the string to check:")
x=sorted(s)
y=sorted(s1)
if len(x) == len(y) :
	if x==y:
		print("s1 is anagram of s")
	else:
		print("s1 is not anagram of s")
else:
	print("s1 is not anagram of s1")
