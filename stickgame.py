import sys


def main():
    turn = 1

    print("Game of stciks")
    sticks = 21
    while sticks >= 0:
        if turn % 2 != 0:
            player1_choose = int(
                input(("Player 1 enter how many sticks to remove: ")))
            if player1_choose != 1 and player1_choose != 2 and player1_choose != 3:
                print("Must remove between 1-3 sticks!")
            else:
                sticks -= player1_choose
                turn += 1
            if sticks <= 0:
                print("Player 2 lost game!")
                sys.exit(0)
            else:
                print(f"There are {sticks} sticks left")
        else:
            player2_choose = int(
                input(("Player 2 enter how many sticks to remove: ")))

            if player2_choose != 1 and player2_choose != 2 and player2_choose != 3:

                print("Must remove between 1-3 sticks!")
            else:
                sticks -= player2_choose
                turn += 1
            if sticks <= 0:
                print("Player 1 lost game!")
            else:
                print(f"There are {sticks} sticksleft")


if __name__ == '__main__':
    main()
