class AgeError(Exception):
    def __init__(self,errorInfo):
        Exception.__init__(self)
        self.errorInfo=errorInfo
    def __str__(self):
        return str(self.errorInfo)+",年龄出错了"
if __name__=="__main__":
    age = int(input("请输入年龄："))
    if age < 0 or age > 150:
        raise AgeError(age)
    else:
        print("great")

