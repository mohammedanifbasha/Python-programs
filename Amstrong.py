num=int(input("enter the number:"))
temp1=num
temp2=num
c=0
while temp1>0:
    c+=1
    temp1=temp1//10
arm=0
while temp2>0:
    d=temp2%10
    arm=arm+d**c
    temp2=temp2//10
if arm==num:
    print("Armstrong")
else:
    print("not Armstrong")