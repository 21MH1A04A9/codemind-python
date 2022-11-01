import math
Number=int(input())
sum=0
squr=math.pow(Number,2)
while squr>0:
    rem=squr%10
    sum=sum+rem
    squr=squr//10
if sum==Number:
    print("Neon Number")
else:
    print("Not Neon Number")