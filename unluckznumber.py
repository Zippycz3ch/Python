# 1-20
# 4 a 13 unluckz
# even numbers x is even 
# odd number x is odd

for x in range(1,21):
    if x % 2 != 0 and x != 13:
        print (f"{x} is odd")
    elif x == 4:
        print(f"{x} is unluckz number")
    elif x == 13:
        print(f"{x} is unlucky number")
    else:
        print(f"{x} is even")
