import pandas as pd
import numpy as np
df1=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8],"C":[9,10,11,12],"D":[13,14,15,16]},index=[1,2,3,4])
df2=pd.DataFrame({"A":[17,18,19,20],"B":[21,22,23,24],"C":[25,26,27,28],"D":[29,30,31,32]},index=[5,6,7,8])
print(pd.concat([df1,df2]))
df3=pd.DataFrame({"B":[1,2,3,4],"C":[5,6,7,8],"D":[9,10,11,12]})
print(pd.concat([df1,df3]))#以行对齐合并
print(pd.concat([df1,df3],axis=1))#以列对齐合并
print(pd.concat([df1,df3],axis=1).dropna(how="any"))#有NAN就去一行
print(pd.concat([df1,df3],axis=1).dropna(how="all"))#全是NAN才去一行
print(pd.concat([df1,df3],axis=1,join="inner"))#保留对的上的
print(pd.concat([df1,df3],axis=1,join="outer"))#保留所有
