##############linear
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
s=pd.read_csv("clim.csv")
print(s)
x=s[["days"]]
print(x)
y=s[["sound"]]
print(y)
w=s[["gas"]]
print(w)
v=s[["humidity"]]
print(v)
z=s[["temp"]]
print(z)
a=int(input("enter the date:"))
c=([[a]])
r=LinearRegression()
r.fit(x,y)
p=r.predict(c)
print("sound:",p)
r.fit(x,w)
q=r.predict(c)
print("gas:",q)
r.fit(x,v)
t=r.predict(c)
print("humidity:",t)
r.fit(x,z)
n=r.predict(c)
print("temp:",n)

















