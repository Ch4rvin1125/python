a=int(input('Enter Any Number:'))
sum=0
while(a>0):
    b=a%10
    sum=sum+b
    a=a//10
   
print("Sum Of Digit Of Number{} is {}.".format(a,sum))
