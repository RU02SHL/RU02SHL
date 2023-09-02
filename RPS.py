import random

def game():
    user = ""
    status = True
    while status == True:
        user = input("""\nPress (R) for Rock
Press (P) for Paper
Press (S) for Scissors
Enter your choice here : """)
        user = user.upper()
        if user == "R":
            print("You have chosen rock")
            status = False
        elif user == "P":
            print("You have chosen paper")
            status = False
        elif user == "S":
            print("You have chosen scissors")
            status = False
        else:
            print("Error : character undefined")
    comp = random.choice(["R","P","S"])
    print(f"\n{user} VS {comp}\n")

    if (user == "R" and comp == "S") or (user == "P" and comp == "R") or (user == "S" and comp == "P"):
        print("You have won !")
    elif user == comp:
        print("It is a tie")
    else:
        print("You have lost.")

print("""Welcome to Rock Paper Scissors.
In this game you choose either rock paper or scissors and so will the computer
Good luck""")
game()

print("Thank You for playing \u2764\uFE0F")