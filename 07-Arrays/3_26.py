import matplotlib.pyplot as plt
import math as M
x=[]
y=[]
for n in range(0,361):
    x = x + [n]

for n in x:
    y=y+[M.sin(M.radians(n))]

plt.plot(x,y)
plt.show()