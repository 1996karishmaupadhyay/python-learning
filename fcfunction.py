from functools import reduce
from itertools import accumulate


def msgl():
    msg="Hi i am local variable from msg"
    #print(msg)
    return msg
msgv=msgl()
print(msgv)


def name(nm):
    print ("Hi i am local variable from name",nm)

def welcome(fn,nm):
    print ("Hi i am local variable from welcome",fn,nm)
welcome(name("John"),"Doe")


lambda a,b: a*b
print((lambda a,b: a*b)(5,6))

num= [1,2,3,4,5,6,17,8,9,]
square =lambda n: n*n
result=map(square,num)
print(list(result))
maxval=reduce(lambda a,b : a if a > b else b,num)
print(maxval)
res1=accumulate(num,lambda a,b : a if a > b else b)
print(list(res1))
re2=filter(lambda n: n%2==0,num)
print(list(re2))

def outer():
    msg="Hi i am local variable from outer"
    msg1="Hi i am local variable from outer msg1"
    def inner():
        nonlocal msg
        msg="Hi i am local variable from inner"
        print(msg)
        print(msg1)
    inner()
outer()

def decorator(func):
    def inner():
        print("Hi i am local variable from decorator")
        func()
        print("Hi i am local variable from decorator inner")
    return inner


@decorator
def display():
    print("Hi i am local variable from display")
display()