from classes.gui import GUI
from classes.board import Board
from classes.player import Player

def main():
    board = Board()

    board.add_player(Player('Player 1', 'white'))
    board.add_player(Player('Player 2', 'black'))
    board.add_player(Player('Player 3', 'red'))

    game_gui = GUI()
    game_gui.run_game()

if __name__ == '__main__':
    main()