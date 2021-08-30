'''input:- {100:'ravi',101:'vijay',102:'rahul',103:'hari'}
output:-
{100: 'ravi', 101: 'vijay', 102: 'rahul', 103: 'hari'}
{'id': 101, 'name': 'rajendra', 'sirname': 'nahar'}
{'id': 102, 'name': 'sheetal', 'sirname': 'golande'}
{'id': 101, 'name': 'rajendra', 'sirname': 'nahar', 'profession': 'manager'}
{'id': 102, 'name': 'sheetal', 'sirname': 'golande', 'salary': 20000}       
{100: 'ram', 101: 'suraj'}
3
dict_keys([100, 101, 102])
dict_values(['ram', 'suraj', 'alok'])
dict_items([(100, 'ram'), (101, 'suraj'), (102, 'alok')])
{100: 'ram', 101: 'suraj', 102: 'alok'}
{}
description: Methods of Dictionary
date: 30-08-2021
Author name: Shruti Nahar'''
data={100:'ravi',101:'vijay',102:'rahul',103:'hari'}
print(data)



#updating pythom dictionary elements

data1={'id':101,'name':'rajendra','sirname':'nahar'}
data2={'id':102,'name':'sheetal','sirname':'golande'}
print(data1)
print(data2)
data1['profession']='manager'
data2['salary']=20000
print(data1)
print(data2)

#del
data={100:'ram',101:'suraj',102:'alok'}
del data[102]
print(data)
#len
data={100:'ram',101:'suraj',102:'alok'}
print(len(data))
#keys
data={100:'ram',101:'suraj',102:'alok'}
print(data.keys())
#values
data={100:'ram',101:'suraj',102:'alok'}
print(data.values())
#items
data={100:'ram',101:'suraj',102:'alok'}
print(data.items())
#clear
data={100:'ram',101:'suraj',102:'alok'}
print(data)
data.clear()
print(data)
