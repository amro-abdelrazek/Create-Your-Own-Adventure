name = input("Insert your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You're on a unknown road, it has come to an end and you can either go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around it and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross the river and were killed by an electric eel.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks old and wobbly, do you want to cross it or head back (cross/head back)? ")

    if answer == "head back":
        print("You head back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you want talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and they bless you up with gold. You WIN! WOHOOOOOO!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for Playing", name)
