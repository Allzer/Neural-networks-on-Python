import numpy as np
import matplotlib.pyplot as plt

def act(x):
    return 0 if x <=0 else 1

def go(c):
    x = np.array([c[0],c[1],1])

    w1 = np.array([1,1,-1.5])
    w2 = np.array([1,1,-0.5])
    weight1 = np.array([w1,w2])
    weight2 = np.array([-1, 1, -0.5])

    sum = np.dot(weight1,x)

    out = [act(x) for x in sum]
    out.append(1)
    out = np.array(out)

    sum = np.dot(weight2,out)

    y = act(sum)
    return y

c1 = [(1,0),(0,1)]
c2 = [(0,0),(1,1)]

print( go(c1[0]), go(c1[1]) )
print( go(c2[0]), go(c2[1]) )



