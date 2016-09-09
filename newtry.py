a=raw_input("Enter a string")
b=len(a)
c=1
print b
print c
while(c<=b):
	print a[0:c:1]
	c=c+1
while(c>=0):
	print a[b-1:c:-1]
	c=c-1
print a[b-1::-1]

