n=int(input())
sum=0
product=1
for i in range (1,n+1):
    sum+=i
    product*=i
choice=input()
if choice=='sum':
    print(sum)
elif choice=='product':
    print(product)