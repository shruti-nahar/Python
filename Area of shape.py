'''input:--
output:-
Area of circle  628.3185307179587
Area of cube   5400
Area of sphere  201.06192982974676
Area of cylinder  87.96459430051421
description: calculate the area of shapes 
date: 25-08-2021
Author name: Shruti Nahar'''
import math
pi=math.pi
def circle(r):
    return 2*pi*r*r
def  cube(side):
    return 6*side*side
def sphere(r):
    return 4*pi*r*r
def cylinder(radius,height):
    return 2*pi*radius + 2*pi*height

print("Area of circle ",circle(10))
print("Area of cube  ",cube(30))
print("Area of sphere ",sphere(4))
print("Area of cylinder ",cylinder(8,6))