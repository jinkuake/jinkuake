import nester
names =("gaoji","jinak","drg")
ages = (18,45,56)
jobs = ("teacher","student","worker")
for names,ages,jobs in zip(names,ages,jobs):
    print("{0}-{1}-{2}".format(names,ages,jobs))