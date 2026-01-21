def room1():
    print("\nROOM 1: LOCKED BEDROOM")
    print("You see a table and a door.")

    choice = input("Where do you check? (table/door): ").lower()

    if choice == "table":
        print("Riddle: What has keys but can't open locks?")
        answer = input("Answer: ").lower()

        if answer == "keyboard":
            print("Correct! Door unlocked.")
            room2()
        else:
            game_over()
    else:
        game_over()


def room2():
    print("\nROOM 2: STUDY ROOM")
    print("You see a computer and a bookshelf.")

    choice = input("What do you inspect? (computer/bookshelf): ").lower()

    if choice == "computer":
        print("Question: What is 5 + 5 * 2?")
        answer = input("Answer: ")

        if answer == "15":
            print("Correct! You move to the next room.")
            room3()
        else:
            game_over()
    else:
        game_over()


def room3():
    print("\nROOM 3: DARK HALL")
    print("A box needs a 3-digit code.")
    print("Hint: First digit is 4, sum of digits is 12.")

    answer = input("Enter the code: ")

    if answer == "444":
        print("Box opened! Final key obtained.")
        room4()
    else:
        game_over()


def room4():
    print("\nROOM 4: EXIT ROOM")
    print("Final Question:")
    print("Which programming language is best for beginners and AI?")

    answer = input("Answer: ").lower()

    if answer == "python":
        print("\nCONGRATULATIONS!")
        print("You escaped all 4 rooms successfully!")
    else:
        game_over()


def game_over():
    print("\nGAME OVER")
    print("Try again!")


def start_game():
    print("WELCOME TO THE 4 ROOM ESCAPE GAME")
    room1()


start_game()
