from random import randint
number = randint(1,10)
user = None
while True:
    user = int(input("Guess a number between 1 and 10: "))
    if user == number:
        print("You won!\nDo you wanna play again? (y/n)")
        hra = input()
        if hra == "y":
            number = randint(1,10)
            user = None
        else:
            print("Thank you for playing")
            break
    elif user > number:
        print("Too high, try again")
    else :
        print("Too low, try again")