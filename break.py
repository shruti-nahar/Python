#input:enter any number5
#      enter any number7
#      enter any number-1 
#output:no. is negative
#       sum is  12    
#description:Break Statement 
#date: 24-08-2021
#Author name: Shruti Nahar
a=0
s=0
n=0
while(a<5):
    n=int(input("enter any number"))
    if(n<0):
          print("no. is negative")
          break
    s=s+n
    a=a+1
print("sum is ",s)
