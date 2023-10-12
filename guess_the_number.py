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

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    guess = -1
    while feedback!='c':
        if low!=high:
            guess = randint(low,high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high(H), too low(L) or Correct(C) ? ").lower()
        if feedback=='h':
            high = guess-1
        elif feedback=='l':
            low = guess+1
    print(f"Yay! The computer guessed your number, {guess}, correctly!")

# Call below function to have computer guess number between 1 to value.
# computer_guess(100) 
# Call below function to have computer pick number between 1 to value, which you can guess.
# guess(100)