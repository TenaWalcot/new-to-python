import matplotlib.pyplot as plt
x1 = [0.75,1.75,2.75,3.75,4.75,5.75,6.75,7.75,8.75,9.75,10.75,11.75,12.75,
13.75,14.75]
x2 = [1.25,2.25,3.25,4.25,5.25,6.25,7.25,8.25,9.25,10.25,11.25,12.25,13.25
,14.25,15.25]
y=[102,134,154,122,143,243,355,342,276,299,241,287,260,231,100]
y2 = [244,250,245,256,234,241,230,267,266,255,248,239,233,221,227]
plt.bar(x1,y,color="green",label="A",width=0.5)
plt.bar(x2,y2,color="#9999ff",label="B",width=0.5)
plt.title("The second graph")
plt.xlabel("time")
plt.ylabel("weight")
plt.legend()
plt.show()