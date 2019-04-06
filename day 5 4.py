import matplotlib.pyplot as plt
import numpy as np
x=range(20)
np.random.seed(1)
y=x+np.random.rand(20)*1.05
plt.figure(figsize=(10,5))
plt.plot(x,y,'.',label="Real number")
plt.plot(x,x,label="fitted line")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()