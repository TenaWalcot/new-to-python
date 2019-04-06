import pandas as pd
left=pd.DataFrame({"A":[0,1,2,3],
                   "B":[4,5,6,7],
                   "key":[8,9,10,11]})
right=pd.DataFrame({"C":[12,13,14,15],
                    "D":[16,17,18,19],
                    "key":[8,9,10,11]})
print(pd.merge(left,right,on ="key"))
left=pd.DataFrame({"first name":["Wang","Fu","Lu","Ding"],
                   "location":[1,2,1,4]})
right=pd.DataFrame({ "last name":["Xu kun","Jia qi","Ai yang","Yi peng"],
                     "location":[1,2,3,5]})
print(pd.merge(left,right,on="location"))
print(pd.merge(left,right,on="location",how="outer"))
print(pd.merge(left,right,on="location",how="inner"))
print(pd.merge(left,right,on="location",how="left"))
print(pd.merge(left,right,on="location",how="right"))
print(pd.merge(left,right,left_on="location",right_on="location"))#左表格按index对齐，右表格按location