num=int(input())
L=num%10
rev=0
c=0
while num:
    r=num%10
    num=num//10
    rev=rev*10+r
    c=c+1
rev=rev%pow(10,c-1)
rev=rev//10

rev=rev*10+L
rev=rev%pow(10,c-1)
rev=r*pow(10,c-1)+rev
print(rev)
