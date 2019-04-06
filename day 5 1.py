import matplotlib.pyplot as plt
import numpy as np
x=[x for x in range(1,16)]
y=[102,134,154,122,143,243,355,342,276,299,241,287,260,231,100]
y2 = [244,250,245,256,234,241,230,267,266,255,248,239,233,221,227]
plt.figure(figsize=(10,5))
plt.plot(x,y,label="A")
plt.plot(x,y2,label="B")
plt.title("The first graph")
plt.xlabel("time")
plt.ylabel("weight")
plt.legend()
plt.show()