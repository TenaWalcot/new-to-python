import seaborn as sns
import numpy as np
x=[x for x in range(1,16)]
y=[102,134,154,122,143,243,355,342,276,299,241,287,260,231,100]
sns.regplot(np.array(x),y)
