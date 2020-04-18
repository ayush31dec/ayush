import random


def check(guess):
    for i in range(3):
        if guess == num:
            print("YES! you are right ")
            break
        elif guess >= num:
            print("Too high ")
            break
        elif guess <= num:
            print("Too low")
            break
        else:
            print("Try again")



num = random.randint(1, 21)
for i in range(3):
    guess = int(input("Enter your Guess "))
    check(guess)
print(num)  
