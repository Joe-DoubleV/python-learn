# random.py

import random
# random.seed(10)
for x in range(10):
	print (random.random(),end = ",")
'''
random.randint()
random.randrange()
random.getrandbits()
random.uniform()
random.choice()
random.shuffle()
'''
print ()
for x in range(10):
	print (random.randrange(10,100,5),end = ' ')
print ()
for x in range(1,10):
	print (random.getrandbits(2),random.getrandbits(4),end = ",")
print ()
for x in range(10):
	print (random.uniform(1,2),end = " ")
listA = [1,2,3,4]
print()
print(random.choice(listA)) 
random.shuffle(listA)
print(listA)