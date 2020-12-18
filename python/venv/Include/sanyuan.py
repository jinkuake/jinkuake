num = input("请输入一个数字")
print(num if int(num)<10 else "false")

score = input("成绩")
if int(score)<60:
    print("不及格")
elif int(score)>60 and int(score)<80:
    print("合格")
elif int(score)>=80:
    print("优秀")