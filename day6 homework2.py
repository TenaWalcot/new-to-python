import numpy as np
import pandas as pd
np.random.seed(15)
s1=np.random.randn(4,4)
data1=pd.DataFrame(s1,columns=["A","B","C","D"])
print(data1)
print(data1.loc[[2],["A","B","C","D"]])
np.random.seed(108)
s2=np.random.randn(4,4)
data2=pd.DataFrame(s2,columns=["A","B","C","D"])
print(data2)
data2.index=['18-01','18-02','18-03','18-04']
print(data2.loc[['18-02','18-03'],["B","C"]])
