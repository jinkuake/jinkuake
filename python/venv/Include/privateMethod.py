class Employee:
    __company = "程序猿"
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def __work(self):
        print("work hard")
        print("age is :{0}".format(self.__age))
        print(Employee.__company)

e=Employee("jinkuake",16)
print(e.name)
print(dir(e))
e._Employee__work()
print(e._Employee__age)
print(Employee._Employee__company)