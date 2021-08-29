#input:Enter the number: 5
#output:Factorial is  120
#description:Find the Factorial of number
#date: 29-08-2021
#Author name: Shruti Nahar
def factorial(num):
    if(num>0):
        if(num==1):
            return num
        else:
            return num*factorial(num-1)
    else:
        print("Invalid Number ")
    
    
num=int(input("Enter the number: "))
print("Factorial is ",factorial(num))