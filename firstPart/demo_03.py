import math

def get_e(num):
	num = int(num)
	temp = pow((1+1/num),num)
	return temp
# for x in range(1,100):
# 	print (round(get_e(pow(2,x)),12))
def dayup(dayfactor):	
	dayup = 1.0
	for x in range(365):
		if x % 7 in [6,0]:
			dayup *= 1 - 0.01
		else:
			dayup *= (1+dayfactor)
	return dayup
df = 0.01
while dayup(df) < 37.78:
	df += 0.00001
print ("{:.6f}".format(df))	
