__author__ = 'deepak.k'
def triangle(base,height):
    area=1.0/2*base*height
    return area

print(triangle(3,4))
def hangeTocelcius(faren):
        celcius=(5.0/9)*(faren-32)
        return celcius
print(hangeTocelcius(30))
a=1
b=1
print(bool(a and b))
c="hello"=="hell"
print(c)
def greet(friend,money):
    if friend and (money>20):
        print("hi")
        money=money-20
    else:
        print("not true")
    return money
greet(True,20)
def areaOfTriangle(a,b,c):
    import math
    s=a+b+c/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    return area
print(areaOfTriangle(2,3,4))
import random
print(random.randrange(1,9))
