'''Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)(s-b)(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.'''
a=int(input())
b=int(input())
c=int(input())
class tri():
    s1 = 0 
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        s = (a+b+c)/2
        self.s1 = (s*(s-a)*(s-b)*(s-c)) * 0.5

class cal(tri):
    def __init__(self,a,b,c):
        tri.__init__(self,a,b,c)

x = cal(a,b,c)
print(x.s1)