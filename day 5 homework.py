import matplotlib.pyplot as plt
Data1 = {'Country': ['US', 'CA', 'GER', 'UK', 'FR'],
         'GDP_Per_Capita': [45000, 42000, 52000, 49000, 47000]}
Data2 = {'Year': [1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010],
         'Unemployment_Rate': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3],
         'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5]}
Data3 = {'Interest_Rate': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
         'Stock_Index_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]}
x=[]
for i in Data1['Country']:
    x.append(i)
y=[]
for i in Data1['GDP_Per_Capita']:
    y.append(i)
plt.figure(figsize=(10,5))
plt.bar(x,y,color="green")
plt.xlabel("country")
plt.ylabel("GDP_Per_Capita")
plt.show()