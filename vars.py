def msgs():
    msg="Hi i am local variable"
    print(msg)
msgs()
gl1="Hi i am global variable"
def msgs1():
    msg="Hi i am local variable from msg1"
    print(gl1,msg)
msgs1()
def msgs2():
    gl1="Hi i am global variable from msg2"
    print(gl1)
msgs2()
print(gl1)
def msgs3():
    global gl1
    gl1="Hi i am global variable from msg3"
    print(gl1)
msgs3()
print(gl1)