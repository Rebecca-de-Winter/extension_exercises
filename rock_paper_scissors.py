import random
def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "You and the computer have both chosen {}. It's a tie.".format()
    