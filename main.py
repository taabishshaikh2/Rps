import random
print("__________WELCOME TO ROCK PAPER SCISSORS___________")
while True:
    ch = int(input("1. Rock\n2. Paper\n3. Scissors\nEnter your choice: "))
    while 3 < ch < 1:
        ch = int(input("Enter valid choice"))
    if ch == 1:
        choice_name = "Rock"
    elif ch == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"
    print(f"Your choice is: {choice_name}")
    print("Now computer's turn")
    comp_ch = random.randint(1, 3)
    if comp_ch == 1:
        comp_choice_name = "Rock"
    elif comp_ch == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"
    print(f"Computer's choice is: {comp_choice_name}")
    print(f"{choice_name} VS {comp_choice_name}")
    if (ch == 1 and comp_ch == 2) or (ch == 2 and comp_ch == 1):
        print("Paper Wins")
        result = "Paper"
    elif (ch == 1 and comp_ch == 3) or (ch == 3 and comp_ch == 1):
        print("Rock Wins")
        result = "Rock"
    else:
        print("Scissors Wins")
        result = "Scissors"

    if result == choice_name:
        print("You Win")
    else:
        print("Computer Wins")
    print("Do you wish to play again? Press 'Y' for Yes and 'N' for No")
    ans = input()
    if ans == 'N' or 'n':
        break


