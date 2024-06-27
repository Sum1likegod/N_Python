# lets make snake gun water game
import random


class Win:
    def __init__(self, users, comp):
        self.users = users
        self.comp = comp

    def win(self):
        if (users == 0 and comp == 1) or (users == 1 and comp == 2) or (users == 2 and comp == 0):
            print("\t\tYou win")


class Lose(Win):
    def __init__(self, users, comp):
        self.users = users
        self.comp = comp

    def lose(self):
        if (users == 0 and comp == 2) or (users == 1 and comp == 0) or (users == 2 and comp == 1):
            print("\t\tYou Lose")


class Draw(Lose):
    def __init__(self, users, comp):
        self.users = users
        self.comp = comp

    def draw(self):
        if (users == comp):
            print("\t\tThe game is draw")


# users.center


while True:
    users = int(input("0 for snake 1 for water and 2 for gun\nAnd 10 for quitting the game\nEnter your choice: "))
    if users == 10:
        print("Thank you for playing")
        break
    comp = random.randint(0, 2)
    print(f"Your's choice is {users} and computer's choice is {comp}")
    result = Draw(users, comp)
    result.win()
    result.lose()
    result.draw()
