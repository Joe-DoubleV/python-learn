import math
import random
import time
print ("PI={}".format(math.pi))

for i in range(1,11):
	Pi = 0
	N = 2*i
	for x in range(N):
		Pi += 1/pow(16,x)*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6))
	print (" PI={},N={}".format(Pi,N))
	print ("ΔPI={}".format(abs(Pi - math.pi)))

Darts = 100
hits = 0
start = time.perf_counter()
for x in range(1,Darts+1):
	x,y = random.random(),random.random()
	dist = pow(x**2+y**2,0.5)
	if(dist <= 1):
		hits += 1
pi = 4 * (hits/Darts)
print ("PI={}".format(pi))
print ("Run Time is {:.5f}s".format(time.perf_counter() - start))	
