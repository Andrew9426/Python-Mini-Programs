#This is an xo game.
class Board():
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
    def display(self):
        """" Display the empty cells """
        print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))
        print("- - - - - -")
        print(" %s | %s | %s " % (self.cells[4], self.cells[5], self.cells[6]))
        print("- - - - - -")
        print(" %s | %s | %s " % (self.cells[1], self.cells[2], self.cells[3]))

    def update_cell(self, cell_no, player):
        """" verify if the cell is allready occupied """
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player
        else:
            print("Please try another cell")

    def draw(self):
        """" return draw if all the cells are occupied, and there are no winner """
        if self.cells[1] != " " and self.cells[2] != " " and self.cells[3] != " " and self.cells[4] != " " and self.cells[5] != " " and self.cells[6] != " " and self.cells[7] != " " and self.cells[8] != " " and self.cells[9] != " ":
            return True
        else:
            return False


    def winner(self, player):
        """" check if one of the players win"""

        if self.cells[1] == player and self.cells[2] == player and self.cells[3] == player:
            return True
        elif self.cells[4] == player and self.cells[5] == player and self.cells[6] == player:
            return True
        elif self.cells[7] == player and self.cells[8] == player and self.cells[9] == player:
            return True
        elif self.cells[1] == player and self.cells[4] == player and self.cells[7] == player:
            return True
        elif self.cells[2] == player and self.cells[5] == player and self.cells[8] == player:
            return True
        elif self.cells[3] == player and self.cells[6] == player and self.cells[9] == player:
            return True
        elif self.cells[3] == player and self.cells[5] == player and self.cells[7] == player:
            return True
        elif self.cells[1] == player and self.cells[5] == player and self.cells[9] == player:
            return True

        return False


#create a board
board = Board()

def print_Wellcome():
    print("Wellcome to the game :D\n ")

def refresh_screen():
    """clear the screen"""
    import os
    os.system("cls")

    print_Wellcome() #Print the header

    board.display() #Show the board

while True:
    refresh_screen()

    x = int(input("\n(X's turn) Please choose 1 - 9. -->")) #Get X input

    board.update_cell(x, "X") #update board

    refresh_screen()  #Refresh screen

    #Check if X won
    if board.winner("X"):
        print("\nX wins!!!\n")
        play_again = input("Do you want to play again? (Y/N) -->").upper()
        if play_again == "Y":
            board.__init__()
            continue
        else:
            break

    #Check for draw
    if board.draw():
        print("\nDraw!\n")
        play_again = input("Do you want to play again? (Y/N) -->").upper()
        play_again = input("Do you want to play again? (Y/N) -->").upper()
        if play_again == "Y":
            board.__init__()
            continue
        else:
            break

    #Get 0 input
    o = int(input("\n(0's turn) Please choose 1 - 9. -->"))

    # update board
    board.update_cell(o, "0")

    # Check if 0 won
    if board.winner("0"):
        print("\n0 wins!!!\n")
        play_again = input("Do you want to play again? (Y/N) -->").upper()
        if play_again == "Y":
            board.__init__()
            continue
        else:
            break

    #Check for draw
    if board.draw():
        print("\nDraw!\n")
        play_again = input("Do you want to play again? (Y/N) -->").upper()
        play_again = input("Do you want to play again? (Y/N) -->").upper()
        if play_again == "Y":
            board.__init__()
            continue
        else:
            break










