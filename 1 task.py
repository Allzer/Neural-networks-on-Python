import numpy as np

def act(x):
    return 0 if x < 0.5 else 1

def go(house, rock, face):
    x = np.array([house, rock, face])

    w1 = [0.3,0.3,0]
    w2 = [0.5, -0.6, 1]

    weight1 = np.array([w1,w2])
    weight2 = np.array([-1,1])

    sum = np.dot(weight1,x)
    out = np.array([act(x) for x in sum])

    sum = np.dot(weight2, out)
    y = act(sum)

    return y

res = go(house=1, rock=0, face=1)

if res >= 0.5:
    print("Good")
else:
    print("Bad")



