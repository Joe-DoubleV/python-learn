
def Fou(num):
	if num == 1:
		return 1
	if num == 2:
		return 1
	if num > 2:
		return Fou(num-1) + Fou(num -2)

def Foufor(num):
	num = int(num)
	a = 1
	b = 1
	if (num == 1 or num == 2):
		return 1
	if num == 3 :
		a = 1
		b = 1
	else:
		for x in range(3,num):
			temp = a
			a = b
			b = b + temp
	return a + b
for x in range(1,10):
	print (f"Fou({x}):",Foufor(x))