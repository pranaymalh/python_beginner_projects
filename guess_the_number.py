from random import randint

def guess(x):
    num = randint(1,x)
    guess = 0
    while guess!=num:
        guess = int(input(f"Guess a number between 1 and {x} : "))
        if guess<num:
            print("Try again. Your guess is too low.")
        elif guess>num:
            print("Try again. Your guess is too high.")
    print(f"Yay! you guessed the number {num} correctly.")

guess(100)