'''
Input:-
Output:-
append()  ['shruti', 21, 'shubham', 'prachi']
extend()  ['shruti', 21, 'shubham', 'prachi', 'shiva', 'om']
insert()  ['shruti', 21, 'sheetal', 'shubham', 'prachi', 'shiva', 'om']
pop()  om
Description :-Implementation of List
Date:-29-08-2021
Author: Shruti Nahar'''
list=['shruti',21,'shubham']
list.append("prachi")
print("append() ",list)
list.extend(['shiva','om'])
print("extend() ",list)
list.insert(2,"sheetal")
print("insert() ",list)
print("pop() ",list.pop())
