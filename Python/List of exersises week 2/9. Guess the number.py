import random
import sys
n=0
gen=random.randint(1,100)
while n!=gen:
    n=int(input())
    if n>gen:
        print('Too large.')
    else: print('Too small.')
print(f'Nailed it! The number is : {n}!')