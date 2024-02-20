import pyfiglet
import random
from colorama import Fore, Style

def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()


def show():
    for row in game_board:
        for cell in row:
            if cell == "X":
                print(Fore.RED + cell, end=" ")
            elif cell == "O":
                print(Fore.GREEN + cell, end=" ")
            else:
                print(cell, end=" ")
        print(Style.RESET_ALL)  

def check_game():
        if game_board[0][0] =="X" and game_board[0][1] =="X" and game_board[0][2] == "X":
            return "Player 1 wins"
        elif game_board[1][0] =="X" and game_board[1][1] =="X" and game_board[1][2] == "X":
            return "Player 1 wins"
        elif game_board[2][0] =="X" and game_board[2][1] =="X" and game_board[2][2] == "X":
            return "Player 1 wins"
        elif game_board[0][0] =="X" and game_board[1][0] =="X" and game_board[2][0] == "X":
            return "Player 1 wins"
        elif game_board[0][1] =="X" and game_board[1][1] =="X" and game_board[2][1] == "X":
            return "Player 1 wins"
        elif game_board[0][2] =="X" and game_board[1][2] =="X" and game_board[2][2] == "X":
            return "Player 1 wins"
        elif game_board[0][2] =="X" and game_board[1][1] =="X" and game_board[2][0] == "X":
            return "Player 1 wins"
        elif game_board[0][0] =="X" and game_board[1][1] =="X" and game_board[2][2] == "X":
            return "Player 1 wins"
        elif game_board[0][0] =="O" and game_board[0][1] =="O" and game_board[0][2] == "O":
            return "Player 2 wins"
        elif game_board[1][0] =="O" and game_board[1][1] =="O" and game_board[1][2] == "o":
            return "Player 2 wins"
        elif game_board[2][0] =="O" and game_board[2][1] =="O" and game_board[2][2] == "O":
            return "Player 2 wins"
        elif game_board[0][0] =="O" and game_board[1][0] =="O" and game_board[2][0] == "O":
            return "Player 2 wins"
        elif game_board[0][1] =="O" and game_board[1][1] =="O" and game_board[2][1] == "O":
            return "Player 2 wins"
        elif game_board[0][2] =="O" and game_board[1][2] =="O" and game_board[2][2] == "O":
            return "Player 2 wins"
        elif game_board[0][2] =="O" and game_board[1][1] =="O" and game_board[2][0] == "O":
            return "Player 2 wins"
        elif game_board[0][0] =="O" and game_board[1][1] =="O" and game_board[2][2] == "O":
            return "Player 2 wins"
        elif game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
            return "Computer wins"
        elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
            return "Computer wins"
        elif game_board[2][0] =="O" and game_board[2][1] =="O" and game_board[2][2] == "O":
            return "Computer wins"
        elif game_board[0][0] =="O" and game_board[1][0] =="O" and game_board[2][0] == "O":
            return "Computer wins"
        elif game_board[0][1] =="O" and game_board[1][1] =="O" and game_board[2][1] == "O":
            return "Computer wins"
        elif game_board[0][2] =="O" and game_board[1][2] =="O" and game_board[2][2] == "O":
            return "Computer wins"
        elif game_board[0][2] =="O" and game_board[1][1] =="O" and game_board[2][0] == "O":
            return "Computer wins"
        elif game_board[0][0] =="O" and game_board[1][1] =="O" and game_board[2][2] == "O":
            return "Computer wins"
        else: return "Draw"
  
title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")
print(title)
n = int(input("2 players enter 1 and single player enter 2 : "))
if n == 1 :

    game_board = [["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]]
    show()
    while True:
        while True:
            print("player 1")
            row = int(input("row: "))
            col = int(input("col: "))
            if 0 <= row <= 2 and 0 <= col <= 2:

                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    break
                else:
                    print("Again")
            else:
                print("Type correctly")
            
        show()
        result = check_game()
        if result != "Draw":
            print(result)
            break 


        print("player 2")
        while True:
            row = int(input("row: "))
            col = int(input("col: "))
            if 0 <= row and row<= 2 and 0 <= col and col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = "O"
                    break
                else:
                    print("Again")
            else:
                print("Type correctly")
            
        show()
        result = check_game()
        if result != "Draw":
            print(result)
            break
else:
    game_board = [["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"]]
    show()
    while True:
        while True:
            print("player 1")
            row = int(input("row: "))
            col = int(input("col: "))
            if 0 <= row <= 2 and 0 <= col <= 2:

                if game_board[row][col] == "-":
                    game_board[row][col] = "X"
                    break
                else:
                    print("Again")
            else:
                print("Type correctly")
            
        show()
        result = check_game()
        if result != "Draw":
            print(result)
            break

        print("Computer")
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)

            if game_board[row][col] == "-":
                game_board[row][col] = "O"
                break

        show()
        result = check_game()
        if result != "Draw":
            print(result)
            break