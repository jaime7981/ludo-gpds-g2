from classes.gui import GUI
from classes.board import Board
from classes.player import Player

import time

def main():
    board = Board()

    board.add_player(Player('Player 1', 'red'))
    board.add_player(Player('Player 2', 'green'))
    board.add_player(Player('Player 3', 'yellow'))
    board.add_player(Player('Player 4', 'blue'))

    board.setup_game()

    print(board.off_board_pieces)

    game_gui = GUI()
    game_gui.run_game()

if __name__ == '__main__':
    main()