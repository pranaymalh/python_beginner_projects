from random import choice

def play():
    user_choice = input("What is your choice? Rock(r), Paper(p) or Scissor(s) ? ")
    computer_choice = choice(['r','p','s'])

    if user_choice==computer_choice:
        print("It is a tie :|")
    elif is_win(user_choice,computer_choice):
        print("You won! :)")
    else:
        print("You lost :(")

def is_win(user_choice,computer_choice):
    if (user_choice=='r' and computer_choice=='s')\
    or (user_choice=='s' and computer_choice=='p')\
    or (user_choice=='p' and computer_choice=='r'):
        return True
    return False

play()