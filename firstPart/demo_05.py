# time 
import time as t

print (t.time(),t.ctime(),'\t')
print (t.strftime("%Y-%m-%d %H:%M:%S",t.gmtime()))
print (t.strftime("%Z",t.gmtime()))
print (t.strptime("2019-07-12 05:52:00","%Y-%m-%d %H:%M:%S"))
