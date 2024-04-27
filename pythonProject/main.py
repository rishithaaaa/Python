import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
d=pd.read_csv('Tata-steel.csv')
x=d['Date']
y=d['Open Price']

#Bar chart
#plt.xlabel('Date',frontsize=18)
#plt.label('Open Price',frontsize=16)
#plt.bar(x,y)

#Pie chart

plt.show()
