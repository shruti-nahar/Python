'''input:- --
output:-
(1, 2, 3)
1     
2     
3     
MUMBAI
(1, 2, 3, 'MUMBAI')
1
(1, 2, 3, 'MUMBAI')
A
(1, 2, 3, 4, 5, 6)
(1, 2, 3, ['english', 'python'])
1
3
('physic', 'chemistry', 1987, 8976)
(1, 2, 3, 4, 5)
('a', 'b', 'c', 'd')
()
(50,)
tup1[0]: physic
tup2[1:5]: (2, 3, 4, 5)
(12, 34.56, 'abc', 'xyz')
('physics', 'chemistry', 1997, 2000)
After deleting tup :        
description:Implementation of tuple and use of its method
date: 25-08-2021
Author name: Shruti Nahar'''

my_tuple=(1,2,3)#create tuple
print(my_tuple)
my_tuple2=(1,2,3,'MUMBAI')#access elements
for x in my_tuple2:
     print(x)
print(my_tuple2)
print(my_tuple2[0])
print(my_tuple2[:])
print(my_tuple2[3][4])

my_tuple=(1,2,3)
my_tuple=my_tuple+(4,5,6)#add elements
print(my_tuple)
my_tuple=(1,2,3,['hindi','python'])
my_tuple[3][0]='english'#it will replace that position
print(my_tuple)
print(my_tuple.count(2))#count no 
print(my_tuple.index(['english','python']))#display index
tup1=('physic','chemistry',1987,8976);
print(tup1)
tup2=(1,2,3,4,5);
print(tup2)
tup3="a","b","c","d";
print(tup3)
#the empty tuple is written as two paraentheses contain nothing
tup1=();
print(tup1)
#to write a tuple containg a single value you have to include a comma,even
#though their is only one value
tup1=(50,)
print(tup1)
tup1=('physic','chemistry',1987,8976);
print("tup1[0]:",tup1[0]);
tup2=(1,2,3,4,5);
print("tup2[1:5]:",tup2[1:5]);
'''Updating Tuples
Tuples are immutable which means you cannot update or change the values of
tuple elements. You are able to take portions of
existing tuples to create new tuples as the following example demonstrates −'''
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3);
'''Delete Tuple Elements
Removing individual tuple elements is not possible. There is, of course, nothing wrong
with putting together another tuple with
the undesired elements discarded.'''
tup = ('physics', 'chemistry', 1997, 2000);
print (tup);
del tup;
print ("After deleting tup : ");
print (tup);

      
