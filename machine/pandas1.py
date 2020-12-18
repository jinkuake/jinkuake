import pandas as pd
from pandas import Series, DataFrame

data = {"name": ["yahoo", "google", "facebook"], "marks": [200, 400, 800], "price": [9, 3, 7]}
f1=DataFrame(data)
print(f1)
f3 = DataFrame(data, columns=['name', 'price', 'marks', 'debt'], index=['a','b','c'])

print(f3)
newdata = {"lang":{"firstline":"python","secondline":"java"}, "price":{"firstline":8000},"time":{"second":"1000"}}

f4 = DataFrame(newdata)
print(f4)
print(f4.columns)
print(f4.price)
sdebt = Series([2.2, 3.3], index=["a","b"])
f3["debt"]=sdebt
f3["price"]["c"]= 300
print(f3)
