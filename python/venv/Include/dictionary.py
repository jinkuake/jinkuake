a = {'name':'qiaoqi','age':16}
b = dict(name='guqi',age = 19)
c = dict([("name","fenghua"),("age",19)])

k = ['name','age']
v = ['guibu',10]
d = dict(zip(k,v))

tb = [a,b,d]
print(tb[2].get("age"))
def f1(a,b,**c):
    print(a,b,c)

f1(1,2,name='flag',age=17)

def f2(*a,b,c):
    print(a,b,c)
f2(20,b=2,c=3) 