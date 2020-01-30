import numpy as np

def pySum():
    a = np.array([0,1,2,3,4])

    b = np.array([9,8,7,6,5])

    c = a**3+b**3

    print(c)

    c = np.arange(12).reshape(3,4)

    print(c)
    
    print("ndarray对象属性")
    print(".ndim,.shape,.size,.dtype,.itemsize")
    print(c.ndim,c.shape,c.size,c.dtype,c.itemsize)
    print(np.int32)
    print(np.ones((2,3)))
    print(np.zeros((3,2)))
    print(np.full((2,2),3))
    print(np.eye(5))
    print(np.ones_like(a))
    print(np.zeros_like(c))
    print("==================")
    print(np.linspace(2.1,5.1,5,endpoint=True))
    a = np.concatenate((np.ones((2,3),dtype=np.int32),np.zeros((2,3),dtype=np.int32)))
    print(a)
    b = np.concatenate((np.ones((2,3)),np.zeros((2,3))),axis=1)
    print(b)
    # print(np.concatenate((np.ones((2,3)),np.zeros((2,3))),axis=2))
    print("=========")
    print(a.reshape((2,6)))
    print(a)
    a.resize((2,6))
    print(a)
    print(a.astype(np.float))
    print("-----------------")
    d = np.arange(12).reshape(3,4)
    print(d)
    print(d[1:3,-2])
    d.resize(2,3,2)
    print(d)
    print(d[1,2,1])

    e = np.arange(24).reshape(2,3,4)
    print(e)
    print(e[:,1:3,::2])
    print(e[:,1:3,0])
    print(e[:,1:3,:])
    print("----------------")
    print(np.sqrt(e))
    print(np.square(e))
    e = e+1
    print(np.log(e))
    print(np.log10(e))
    print(np.log2(e))
    print(np.exp(e))

    print(np.mod(e+10,e+1))

    print(np.maximum(e,np.sqrt(e)))

    print(e-2>np.sqrt(e))
    # print(a[1:4])
    return c

if __name__ == '__main__':
    pySum()
