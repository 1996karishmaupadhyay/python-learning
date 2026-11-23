def hi():
    print("Hello, world!")
hi()
def num(x):
    print("The number is ",x)
num(10)
def numb(x,y=20):
    print("The numbers are ",x,y)
numb(10)
def details(name,age):
    print("My name is ",name," and my age is ",age)
details("Alice",25)
details(23,"Bob")#wrong output because of wrong order of arguments
def fullname(firstname,lastname):
    print("My full name is ",firstname,lastname)
fullname(lastname="Smith",firstname="John")#correct output because of keyword arguments
def fulln(*nam):
    for name in nam:
     print(name)
    print("My full name is ",nam)
fulln("John","Smith","Doe")
def fn(**fullname):
    for k,v in fullname.items():
     print(k,v)
fn(firstname="John",lastname="Smith",middlename="Doe")

def f1(x):
    n="Hello, world! hjvfgs"
    def f2():
        print(n)
    p="karishma"
    print(p)
    f2()
f1(10)