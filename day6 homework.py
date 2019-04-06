import pandas as pd
import numpy as np
s1=pd.Series([x for x in range(1,6)],index=[x for x in range(5)])
print(s1)
for i in range(5):
    s1[i]=float(s1[i])
s1[4]=np.NAN
s1.index=["h","i","j","k","l"]
print(s1)
data1=pd.DataFrame(s1)
print(data1)