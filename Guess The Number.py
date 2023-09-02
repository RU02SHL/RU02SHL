import random

#Computer guesses number game

def comp():
    print("""Hello,
    Welcome to Guess The Number Computer edition.
    In this game, the computer tries to guess a number that is you choose.
    The computer get 10 guesses.
    The range is from 1 to 100
          """)
    
    x = 1
    y = 100
    guesses = 10
    hlc = ""
    while (hlc.upper() != "C") and (guesses > 0):
        if x != y:
            guess = random.randint(x,y)
        else:
            guess = x
        print(f"The computer guesses {guess}")
        hlc = input("""If the number is higher press (H)
If the number is lower press (L)
If the number is correct press (C)
Enter your answer here : """)
        if hlc.upper() == "H":
            x = guess
        if hlc.upper() == "L":
            y = guess
    if guesses == 0:
            print("\nYou Win ! Well done\n")
    if hlc.upper() == "C":
        print("You lost.")
    
    print("Thank You for playing \u2764\uFE0F")
    return

#'User guesses number game

def user():
    print("""Hello,
    Welcome to Guess The Number User edition.
    In this game, you try to guess a number that is randomly generated.
    You get 10 guesses.
    Easy : 0-10
    Intermediate : 0 - 100
    Professional : 0 - 1000
    Godly : 0 - 10000""")
#easy mode
    def easy():
        easy = random.randint(1,10)
        guess = 0
        guesses = 10
        while (guess != easy) and (guesses > 0):
            guess = int(input("Enter your guess : "))
            if guess < easy:
                print("higher")
                guesses -= 1
            elif guess > easy:
                print("lower")
                guesses -= 1
        if guesses == 0:
            print("\nYou ran out of guesses\n")
        if guess == easy:
            print("\nYou won ! Well done.\n")
        return
#intermediate mode
    def intermediate():
        intermediate = random.randint(1,100)
        guess = 0
        guesses = 10
        while (guess != intermediate) and (guesses > 0):
            guess = int(input("Enter your guess : "))
            if guess < intermediate:
                print("higher")
                guesses -= 1
            elif guess > intermediate:
                print("lower")
                guesses -= 1
        if guesses == 0:
            print("\nYou ran out of guesses\n")
        if guess == intermediate:
            print("\nYou won ! Well done.\n")
        return
#profesional mode
    def profesional():
        profesional = random.randint(1,1000)
        guess = 0
        guesses = 10
        while (guess != profesional) and (guesses > 0):
            guess = int(input("Enter your guess : "))
            if guess < profesional:
                print("higher")
                guesses -= 1
            elif guess > profesional:
                print("lower")
                guesses -= 1
        if guesses == 0:
            print("\nYou ran out of guesses\n")
        if guess == profesional:
            print("\nYou won ! Well done.\n")
        return
#godly mode
    def godly():
        godly = random.randint(1,10000)
        guess = 0
        guesses = 10
        while (guess != godly) and (guesses > 0):
            guess = int(input("Enter your guess : "))
            if guess < godly:
                print("higher")
                guesses -= 1
            elif guess > godly:
                print("lower")
                guesses -= 1
        if guesses == 0:
            print("\nYou ran out of guesses\n")
        if guess == godly:
            print("\nYou won ! Well done.\n")
        return
#main game loop
    status = True
    while status == True:
        level = input("Please enter the level you want to play : ")
        if level.upper() == "EASY":
            print("Easy mode selected")
            print("")
            easy()
            status = False
        elif level.upper() == "INTERMEDIATE":
            print("Intermediate mode selected")
            print("")
            intermediate()
            status = False
        elif level.upper() == "PROFESIONAL":
            print("Profesional mode selected")
            print("")
            profesional()
            status = False
        elif level.upper() == "GODLY":
            print("Godly mode selected")
            print("")
            godly()
            status = False
        else:
            print("Error : level not recognised, please try again.")


    print("Thank You for playing \u2764\uFE0F")

# give the user an option between games

status = True
while status == True:
    version = input("""Press 1 to guess the computer's number
Press 2 to have the computer guess your number
Enter your choice here : """)
    if version == "1":
        user()
        status = False
    elif version == "2":
        comp()
        status = False
    else:
        print("Error : input not recognised")


