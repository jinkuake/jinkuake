class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self,salary):
        if 1000<salary<5000:
            self.__salary = salary
        else:
            print("wrong number")
emp1 = Employee("jinkuake",5555)
print(emp1.salary)
emp1.salary = 2000
print(emp1.salary)