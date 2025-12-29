#raise

# salary = float(input("ENter Salary"))

# if salary < 0:
#     raise ValueError("salary cannot nagetive")
# else:
#     print("salary",salary)


age = float(input("ENter age"))

if age < 0:
    # raise ValueError("age cannot nagetive")
    raise Exception("age cannot nagetive")
else:
    if age>= 18:
        print("vote")
    else :
        print("not vote")