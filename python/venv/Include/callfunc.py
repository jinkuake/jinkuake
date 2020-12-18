class SalaryAccount:
  def __call__(self, salary):
        print("算工资---")
        yearSalary = salary * 12
        daySalary = salary//22.5
        return dict(yearSalary=yearSalary, daySalary=daySalary)

s = SalaryAccount()
print(s(8000))