#lambda 

# def add(a):
#     return a+1
# res =add(1)
# print(res)

# SYNTAX
# lambda argument :expression

# fun = lambda a,b:a+b
# res = fun(2,4)
# print(res)


#--------------
#filter (function, sequence)
# seq = [1,2,3,4]
# odd = lambda x: True if x % 2 != 0 else False
# foutput=filter(odd,seq)
# print(foutput)
# print(list(foutput))


#---------filter
seq = [1,2,3,4]
foutput= filter(lambda x: True if x % 2 != 0 else False, seq)

print(foutput)
print(list(foutput))

#--------map 

# seq = [1,2,3,4]
# moutput= map(lambda x: True if x % 2 != 0 else False, seq)

# print(moutput)
# print(list(moutput))


seq = [1,2,3,4]
moutput= map(lambda x: x ** 2, seq)

print(moutput)
print(list(moutput))

