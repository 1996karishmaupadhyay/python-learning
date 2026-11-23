def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))

def printnum(n):
    if(n==0):
        return
    else:
        print(n)
        printnum(n-1)
printnum(5)

def printnum1(n):
    if(n==0):
        return
    else:
        printnum1(n-1)
        print(n)
printnum1(5)