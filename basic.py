print("Hi Karishma you are too good!")
#name=input("Hi,Enter your name : ")
#print("My name is ",name)
name="Karishma"
age=30
dob="1996-07-01"
print(name,age,dob)
school ,year="ABC School",2023
print(school,year)
#intnum=int(input("Enter an integer number : "))#ValueError: invalid literal for int() with base 10: '5.55'
#print(intnum)
_name="variable name can start with underscore"
print(_name)
#1_name="variable name cannot start with number"
#print(1_name)
fruits=["apple","banana","mango"]
print(fruits)
print(type(fruits))
vegetables=("carrot","potato","onion")
print(vegetables)
for vegetable in vegetables:
    print(vegetable)
print(type(vegetables))
my_age=19
print(my_age)
if my_age>=20:
    print("You are eligible to vote")
elif my_age>=18 and my_age<20:
    print("You are not eligible to vote but you can apply for voter ID")
else:
    print("You are not eligible to vote")
    
    
n=10
for i in range(0,n):
    print(i)