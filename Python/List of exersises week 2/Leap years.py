year=int(input())

if year%4==1:
    year-=1
elif year%4==2:
    year-=2
elif year%4==3:
    year-=3
for i in range (1,21):
    year += 4
    print(year)