import pandas as pd
df=pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],columns=["A","B","C","D"])
print(df[df["A"]>3])
print(df[df<10])
print(df[(df<10)&(df>3)])