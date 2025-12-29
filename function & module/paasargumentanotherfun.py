# def add_1(number):
#     return number +1 

# def sqre(number):
#     return number **2

# num=int(input("Enter num "))
# res_1 = add_1(num)
# res_2 = sqre(res_1)
# print(f"output is : {res_2}")



def add_1(number):
    return number +1 

def sqre(number):
    return number **2

num=int(input("Enter num "))
res_1 = sqre(add_1(num))
print(f"output is : {res_1}")
