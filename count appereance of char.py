'''input:aaabbbbbbccccdddddd
output:-the letter a is  3 times
        the letter b is  6 times
        the letter c is  4 times
        the letter d is  6 times
description: Count the appereance of char in string
date: 26-08-2021
Author name: Shruti Nahar'''
msg="aaabbbbbbccccdddddd"
print(msg)
count=0
con=0
c=0
d=0
for i in range(0,len(msg)):
     if msg[i]=='b':
          count=count+1
     elif msg[i]=='a':
         con=con+1
     elif msg[i]=='c':
         c=c+1
     else:
         d=d+1


print("the letter a is ",con,"times")
print("the letter b is ",count,"times")
print("the letter c is ",c,"times")
print("the letter d is ",d,"times")