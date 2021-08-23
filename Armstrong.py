#input:-Enter the num 153
#output:-Armstrong number
#description:Check whether the number is armstrong or not
#date: 23-08-2021
#Author name: Shruti Nahar
num=int(input("Enter the num "))
sum=0
temp=num
x=len(str(num))
while(temp>0):
    r=temp%10
    sum=sum+r**x
    temp=temp//10
if(num==sum):
    print("Armstrong number ")
else:
    print("Not a Armstrong number")