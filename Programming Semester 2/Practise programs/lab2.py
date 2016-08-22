'''
The Problem

We are going to experiment with overloaded operators and making our own class. We are going to make a 2D vector class.
Some Background

A vector is basically an arrow that has a magnitude (a length) and a direction (an angle with respect to typically the x axis). It usually is represented as an
x,y pair, where the origin of the vector is a 0,0 and the head of the vector is at the listed pair.
Here are some of the operations you can perform on a vector.

vector addition. If V1 is (x,y) and V2 is (a,b), the V+W is (x+a,y+b), a vector
vector multiplication by a scalar. if V1 is (x,y), the V*n is (x*n,y*n), a vector
vector subtraction V-W is the same as V+(W*-1), a vector
vector multiplication with another vector. There are two possibilities, dot product or cross product. We’ll do dot product. If V=(x,y) and W=(a,b),
then V*W = x*a + y*b, a scalar. Thus the dot product yields a scalar, not a vector
vector magnitude. The magnitude based on the Pythagorean theorem for a V=(x,y) says that the magnitude is the square root of (x2 + y2) .
Your Tasks

Make a vector class. Provide the operators
__init__ # constructor, takes 3 args: self,x,y . No return
__str__ # for printing, takes 1 arg self. Returns a string
__add__ # vector + vector. Takes 2 args, self and vector. Returns a new vector
__sub__ # vector – vector. Takes 2 args, self and vector. Returns a new vector
__mul__ # two possibilities. vector*integer or vector*vector (dot product). Get it to do just one of the two at first,
# then see if you can use introspection to do both
magnitude # magnitude of the vector. One arg, self. Returns a floa'''

'''Lab 3 Python
Author Ciarán O'Loughlin
Date: 05/2/2015
'''
import math
class vector:
     def __init__(self,x,y):
         self.x=x
         self.y=y

     def __str__(self):
         return "({}, {})".format(self.x,self.y)

     def __repr__(self):
         return self.__str__()
     def __add__(self,other):
         return vector(self.x+other.x,self.y+other.y)
     def __sub__(self,other):
         return vector(self.x-other.x,self.y-other.y)
     def __mul__(self,other):
         return vector(self.x*other,self.y*other)
     def magnitude(self):
         mag=(self.x*self.x)+(self.y*self.y)
         mag=math.sqrt(mag)
         return mag
v1=vector(7,3)
v2=vector(7,6)
vadd=v1.__add__(v2)
vsub=v1.__sub__(v2)
vmul=v1.__mul__(8)
vmag=v1.magnitude()
print("The vectors added together equal {}".format(vadd))
print("The vectors subtracted are {}".format(vsub))
print("{}".format(vmul))
print("{}".format(vmag))
        




