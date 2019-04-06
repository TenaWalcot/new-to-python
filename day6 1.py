import pandas as pd
import numpy as np
s1=pd.Series([x for x in range(5)],index=["a","b","c","d","e"])
print(s1)
print(s1.values)
print(s1.index)
s2=pd.Series([x for x in range(5)],index=["a","b","c","d","e"])
print(s1+s2)
#同index，同数量
data={"A":[1,2,3,4],"B":[5,6,7,8],"C":[9,0,1,2]}
df=pd.DataFrame(data,index=[1,2,3,4])
print(df)
np.random.seed(0)
data2=np.random.randn(5,5)
df2=pd.DataFrame(data2,index=[str(x) for x in range(1,6)],columns=[str(x) for x in range(5)])
print(df2)
print(df2.loc[["1","2"],["3","4"]])
df2["5"]="hhh"
df2["6"]=df2["0"]+df2["1"]+df2["2"]+df2["3"]+df2["4"]
print(df2)