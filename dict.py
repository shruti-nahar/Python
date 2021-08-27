'''input:- --
output:-
{1: 'apple', 2: 'ball'}
Accessing element  apple
len()  2
key()  dict_keys([1, 2])
values()  dict_values(['apple', 'ball'])
dictionary  {1: 'apple', 2: 'ball'}
items()  dict_items([(1, 'apple'), (2, 'ball')])
update()  {1: 'apple', 2: 'ball', 3: 'apple'}
get()  apple
pop()  ball
{1: 'apple', 3: 'apple'}
description: Methods of Dictionary
date: 27-08-2021
Author name: Shruti Nahar'''
my_dict={1:'apple',2:'ball'}
print(my_dict)
print("Accessing element ",my_dict[1])
print("len() ",my_dict.__len__())
print("key() ",my_dict.keys())
print("values() ",my_dict.values())
print("dictionary ",my_dict)
print("items() ",my_dict.items())
my_dict.update({3:'apple'})
print("update() ",my_dict)
print("get() ",my_dict.get(3))
print("pop() ",my_dict.pop(2))
print(my_dict)