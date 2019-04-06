import matplotlib.pyplot as plt
Data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
         'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3],
         'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5]}
Data3 = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
         'Stock_Index_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]}
x=[]
for i in Data2['Year']:
    x.append(i)
y=[]
for i in Data2['Unemployment_Rate']:
    y.append(i)
z=[]
for i in Data2['Interest_Rate']:
    z.append(i)
plt.figure(figsize=(10,5))
plt.plot(x,y,color="orange",label="Unemployment_Rate")
plt.plot(x,z,color="blue",label="Interest_Rate")
plt.xlabel("year")
plt.legend()
plt.show()