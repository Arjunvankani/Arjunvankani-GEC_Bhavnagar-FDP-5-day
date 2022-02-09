#!/usr/bin/env python
# coding: utf-8

# Matplotlib is a Python 2D plotting library that produces high-quality charts and figures, which helps us visualize extensive data to understand better
# 
# In this exercise we will be using Matplotlib to visualize Company Sales Data

# In[1]:


month_number=[1,2,3,4,5,6,7,8,9,10,11,12]
facecream = [2500,2630,2140,3400,3600,2760,2980,3700,3540,1990,2340,2900]
facewash = [1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
toothpaste=[5200,5100,4550,5870,4560,4890,4780,5860,6100,8300,7300,7400]
bathingshop=[9200,6100,9550,8870,7760,7490,8980,9960,8100,10300,13300,14400]
shampoo=[1200,2100,3550,1870,1560,1890,1780,2860,2100,2300,2400,1800]
moisturizer=[1500,1200,1340,1130,1740,1555,1120,1400,1780,1890,2100,1760]
total_units=[21100,18330,22470,22270,20960,20140,29550,36140,23400,26670,41280,30020]
total_profit=[211000,183300,224700,222700,209600,201400,295500,361400,234000,266700,412800,300200]


# # Exercise 1: Plot total profit of all months using line plot with the following Style properties:
# 
# 1) Line Style dotted and Line-color should be red
# 2) Show legend at the lower right location.
# 3) X label name = Month Number
# 4) Y label name = Sold units number
# 5) Add a circle marker.
# 6) Line marker color as red
# 7) Line width should be 3
# 
# 
# ![pic2.png](attachment:pic2.png)

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
y = np.array([100000,200000,300000,400000,500000])
plt.plot(month_number,total_profit,linestyle='dashed',marker='.',markerfacecolor='black',linewidth=3,color='red',markersize=16)
plt.xticks(month_number)
plt.yticks(y)
plt.xlabel("Month Number")
plt.ylabel("Sold units number")
plt.legend(["Profot data of last year"],loc = 'lower right')
plt.title("Comapany Sales data of last year")
plt.show()


# # Exercise 2: Plot all product sales data using a multiline plot
# 
# Display the number of units sold per month for each product using multiline plots. (i.e., Separate Plotline for each product ).
# 
# ![fig3.png](attachment:fig3.png)

# In[3]:



plt.figure(figsize=(9, 5))
lines = ['facewash','facecream','toothpaste','bathingshop','shampoo','moisturizer']


plt.plot(month_number, facewash, 'o-', color='red', label='Face Wash Sales Data')

plt.plot(month_number, facecream, 'o-', color='blue', label='Face Cream Sales Data')

plt.plot(month_number, toothpaste, 'o-', color='green', label='Face Wash Sales Data')

plt.plot(month_number, bathingshop, 'o-', color='red', label='Bathing Shop Sales Data')

plt.plot(month_number, shampoo, 'o-', color='purple', label='Shampoo Sales Data')

plt.plot(month_number, moisturizer, 'o-', color='brown', label='Moisturizer Sales Data')

plt.xlabel("Month Number")
plt.ylabel("Sales units in number")

plt.title("Comapany Sales data of last year")
plt.xticks(month_number)
plt.legend()
plt.title('Sales data')
plt.show()


# # Ecercise 3: Read toothpaste sales data of each month using a scatter plot. Also, add a grid in the plot. gridline style should “–“.
# 
# ![fig4.png](attachment:fig4.png)
# 
# 

# In[4]:


plt.scatter(month_number, toothpaste,  alpha=0.5)
plt.xticks(month_number)
plt.grid(True, linewidth = "1.4", linestyle = "--") 
plt.xlabel("Month Number")
plt.ylabel("Number of units Sold")
plt.legend(["Tooth paste Sales data"])
plt.title("Tooth paste Sales data")
plt.show()


# # Exercise 4: Plot face cream and facewash product sales data using the bar chart.
# 
# The bar chart should display the number of units sold per month for each product. Add a separate bar for each product in the same chart
# 
# ![fig5.png](attachment:fig5.png)
# 

# In[5]:


plt.figure(figsize=(9, 5))

plt.bar([a-0.25 for a in month_number], facecream, width= 0.25, label = 'Face Cream sales data', align='edge')
plt.bar([a+0.25 for a in month_number], facewash, width= -0.25, label = 'Face Wash sales data', align='edge')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.legend(loc='upper left')
plt.title(' Sales data')
plt.grid(True, linewidth = "1.4", linestyle = "--") 
plt.show()


# # Exercise 5: Plot the total profit of each month using the histogram to see the most common profit ranges
# 
# ![fig6.png](attachment:fig6.png)
# 

# In[6]:


plt.figure(figsize=(9, 5))
labels = ['low', 'average', 'Good', 'Best']

x = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
plt.hist(total_profit,x,label = 'Profit data')

plt.ylabel('Actual Profot in dollar')
plt.xlabel('Profot range in dollar')
plt.title(' Sales data')
plt.xticks(x)
plt.legend(loc='upper left')
plt.title('Profit data')


# # Exercise 6: Plot total sale data for last year for each product using a Pie chart
# 
# 
# ![fig7.png](attachment:fig7.png)

# In[7]:


labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
sales = [sum(facecream), sum(facewash),  sum(toothpaste),  sum(bathingshop), sum(shampoo),  sum(moisturizer)]
plt.axis("equal")
plt.pie(sales, labels=labels, autopct='%1.1f%%')
plt.legend(loc='lower right')
plt.title('Sales data')
plt.show()


# In[ ]:





# In[ ]:




