listA = [x*x for x in range(10) if x%3==0]
print(listA)
def power(x,y,*other):
	if other :
		print("Other:",other)
	return pow(x,y)
p = (5,)*2
print(p)
print(power(*p))