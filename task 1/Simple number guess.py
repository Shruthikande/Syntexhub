import random
num=random.randint(1,100)
print("computer selected number from 1 to 100 (inclusive),now its your turn-")
turns=0
while True:
    guess=int(input("Enter the guessed number="))
    if guess==num:
        print("\n\tYou got it right")
        break
    elif  guess<num:
        print("\tBigger number please")
        turns+=1
    elif guess>num:
        print("\tLesser number please")
        turns+=1
print("\nNumber of turns=",turns+1)