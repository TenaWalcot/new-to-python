import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
Data3 = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
         'Stock_Index_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]}
x=[]
for i in Data3['Interest_Rate']:
    x.append(i)
y=[]
for i in Data3['Stock_Index_Price']:
    y.append(i)
sns.regplot(np.array(x),np.array(y))