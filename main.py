from classes.gui import GUI
from classes.board import Board
from classes.player import Player

def main():
    '''
    board = Board()

    board.add_player(Player('Player 1', 'red'))
    board.add_player(Player('Player 2', 'green'))
    board.add_player(Player('Player 3', 'yellow'))
    board.add_player(Player('Player 4', 'blue'))

    board.setup_game()
    '''
    
    game_gui = GUI()
    game_gui.run_game()

if __name__ == '__main__':
    main()