


n=1 # global variable its a outside a function and inside functio
def fn():
    global n # now its a global 
    n=5  #local variable
    print('in',n)

fn()

print('out',n)