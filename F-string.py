'''input:--
output:-
hello my name is shruti and my age is 20 
hello my name is shruti and my age is 10 
hello my name is shruti and my age is 5  
hello my name is shruti and my age is 8  
hello my name is shruti and my age is 8  
hello my name is shruti and my age is 4  
description:Implementation of F-string
date: 28-08-2021
Author name: Shruti Nahar'''
import random
name="shruti"
age=20
print(f"hello my name is {name} and my age is {age} ")
for i in range(5):
    print(f"hello my name is {name} and my age is {random.randint(0,10)} ")
