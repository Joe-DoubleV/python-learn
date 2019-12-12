import time

scale = 10
print("start".center(20,"-"))

# for x in range(1+scale):
# 	a = '*' * x
# 	b = '.' * (scale - x)
# 	c = (x/scale)*100

# 	print("{:^3.0f}% [{}->{}]".format(c,a,b))
# 	time.sleep(0.51)
# print("End".center(20,"-"))

# for x in range(101):
# 	print("\r{:3}%".format(x), end="")
# 	time.sleep(0.01)
scale = 50
print('\n'+"start".center(scale//2,"-"))
start = time.perf_counter()
for x in range(1+scale):
	a = '*' * x
	b = '.' * (scale - x)
	c = (x/scale)*100
	dur = time.perf_counter() - start
	print("\r{:^3.0f}% [{}->{}]{:.2f}s".format(c,a,b,dur),end='')
	time.sleep(0.1)
print("\r{:^3.0f}% [{}**{}]{:.2f}s".format(c,a,b,dur),end='')
print("\n"+"End".center(scale//2,"-"))