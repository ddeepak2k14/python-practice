__author__ = 'deepak.k'
num=1
def fun():
    global num
    num=6
    return num
def fun1():
    global num
    num=num+2
    return num
print((fun()))
print(num)
print(fun1())
print(num)
