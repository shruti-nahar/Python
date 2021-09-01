a=10
def fun(b):
     c=30
     print("a=",a)
     print("b=",b)
     print("c=",c)
fun(20)
""" to access global variable inside a function use a keyword global"""






d=10
def fun(b):
     c=30
     global d
     d=d+10
     print("d=",d)
     print("b=",b)
     print("c=",c)
fun(20)
