import  numpy as  np
import  matplotlip.pyplot as plt

x=np.linspace(-1,1,100)
y = 2*y**3 -3

plt.figure()
plt.plot(x,y, 'ro-')
