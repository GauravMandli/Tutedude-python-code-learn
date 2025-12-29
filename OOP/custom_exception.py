class salaryError(Exception):
    pass

def get_salary(salary):
    if salary <0:
        raise salaryError("not negative")
    else:
        bonus = 0.1 * salary
        return salary+ bonus
    
salary=int(input("ENter your salary: "))
final_salary=get_salary(salary)
print(final_salary)
