__author__ = 'deepak.k'
print("hello deepak")
import math
print(math.acos(.5))
name=input('what is yopur name')
print('my name is {} as per my knowledge'.format(name))
while True:
    item=input('enter quit to exit')
    if item=='quit':
        break


# if else
i=20
j=25
if i<10:
    print('less than 10')
elif i>15:
    print('hi')
else:
    print('deepu')

#global variable
x=5
def global_fn():
    global x
    print(x)
    x=2
    print(x)
global_fn()