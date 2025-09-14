def employee(name, salary=10000):
    tax = salary * 0.02
    final_salary = salary - tax
    print(name,"'s salary'", final_salary, "after tax")


employee("Ali", 20000)
employee("Sara")
