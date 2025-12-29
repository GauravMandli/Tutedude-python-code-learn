#without recursionn
# def fact(num):
#     factorial =1 
#     while num > 1:
#         factorial *= num
#         num -= 1
    
#     return factorial
# n=5
# print(f"factorial of {n} is {fact(n)}")


def fact(num):
    if num ==1:
        return 1
    else:
        factorial=num * fact(num-1)
        return factorial
print(fact(5))