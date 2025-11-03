'''🔹 2️⃣ Weather Data Analysis

Goal: Find temperature statistics of a week/month.
Hint:

Store daily temperatures in an array.

Find average, max, min using np.mean(), np.max(), np.min().

Identify how many days were above the average temperature using np.where().'''
import numpy as np
a=np.array([10,21,12,40,50,60,80])
print("Weekly temperature report")
print("The temperature in a week :",a)
result=np.mean(a)
print("The average of temperature in a week :",result)
_min=np.min(a)
print("The minimum temperature in a week :",_min)
_max=np.max(a)
print("The maximum temperature in a week :",_max)
b=np.where(a>result)
print("Days above temperature index position is :",b[0])
print("the above average temperature is : ",a[b])
