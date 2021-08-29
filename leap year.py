'''input:Enter the year 2020
output:Leap Year
Description:-Check whether the year is leap or not
date: 29-08-2021
Author name: Shruti Nahar'''
year=int (input("Enter the year "))
if(year%400==0) or (year%4==0):
    print("Leap Year")
elif(year%100==0):
    print("Not a Leap Year ")
else:
    print("Not a Leap Year")