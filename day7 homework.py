import pandas as pd
d1=pd.DataFrame({"A":[1,5,9,13],
                 "B":[2,6,10,14],
                 "C":[3,7,11,15],
                 "D":[4,8,12,16],
                 "E":["H","J","K","L"]})
d2=pd.DataFrame({1:["H","L","J","J"],
                 2:["S","S","T","S"],
                 3:[6,2,5,3]})
print(d1)
print(d2)
print(pd.merge(d1,d2,left_on="E",how="outer",right_on=1))
d3=d1.join(d2,how="inner")
d3[3]=[6.0,2.0,5.0,3.0]
print(d3)













'''
for i in range(4):
    if d3.loc[i,2]=="S":
        p=d3.loc[i,"B"]+d3.loc[i,"C"]-d3.loc[i,3]
        s.append(p)
    if d3.loc[i,2]=="T":
        p=d3.loc[i,"B"]-d3.loc[i,"C"]+d3.loc[i,3]
        t.append(p)
'''