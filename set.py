'''input:--
output:
{1, 2, 3}
{1.0, (1, 2, 3), 'hello'}
{1, 2, 3, 4}
[1, 2, 3, 2]
<class 'dict'>
<class 'set'>
{1, 3}
{1, 2, 3}
{1, 2, 3, 4}
{1, 2, 3, 4, 5, 6, 8}
{1, 3, 4, 5, 6}
{1, 3, 5, 6}
{1, 3, 5}
{1, 3, 5}
{'e', 'l', 'r', 'd', 'o', 'H', 'W'}
e
{'r', 'd', 'o', 'H', 'W'}
set()
set()
{1, 2, 3, 4, 5, 6, 7, 8}
{4, 5}
{1, 2, 3}
{1, 2, 3, 6, 7, 8}
 Description:-Set Operation
date: 29-08-2021
Author name: Shruti Nahar'''
'''we can add or remove '''
my_set={1,2,3}
print(my_set)
#set of mixed data types
my_set={1.0,"hello",(1,2,3)}
print(my_set)
#set cannot have duplicates
#output:{1,2,3,4}
my_set={1,2,3,4,3,2}
print(my_set)

#we can make set from a list
my_set=([1,2,3,2])
print(my_set)

#set cannot have mutable items
#here [3,4]  is amutable list
#this eill cause an error
#my_set={1,2[3,4]}
#distinguish set and dictonary while creating empy set
# intialize a with {}
a={}
#check data type of a
print(type(a))
#intiale a with set()
a=set()
#check data type of a
print(type(a))

#intialize my_set
my_set={1,3}
print(my_set)
#if you uncomment line 9,
#you will get an error
#typeError:set objecty doesnot supporting indexing
#my_set[0]

#add an element
my_set.add(2)
print(my_set)

#add mulitiple elements
#output:{1,2,3,4}
my_set.update([2,3,4])
print(my_set)

#add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)
# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

## WILL  GIVE ERROR my_set.remove(2)


# initialize my_set
# Output: set of unique elements
my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())

# pop another element
my_set.pop()
print(my_set)

# clear my_set
# Output: set()
my_set.clear()
print(my_set)

print(my_set)


# Set union method
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use | operator
# Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(A | B)


# Intersection of sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use & operator
# Output: {4, 5}
print(A & B)


# Difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use - operator on A
# Output: {1, 2, 3}
print(A - B)

# Symmetric difference of two sets
# initialize A and B
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# use ^ operator
# Output: {1, 2, 3, 6, 7, 8}
print(A ^ B)


