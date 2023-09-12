from classes.dice import Dice
import random

NUMBER_OF_SQUARES = 58
BOARD_LOOP = 52
SAFE_SQUARES = 6

OFFSETS = {
    'red': 0,
    'green': 13,
    'yellow': 26,
    'blue': 39
}

class Board():
    def __init__(self) -> None:
        self.players = []
        self.on_board_pieces = []
        self.off_board_pieces = []
        self.dice = Dice()

    
    def add_player(self, player):
        if len(self.players) <= 4:
            self.players.append(player)
        
        else:
            print('Max number of players reached')


    def remove_player(self, player):
        self.players.remove(player)

    
    def setup_players(self, dice_rolls = []):
        # Maybe change dice roll implementation into a gui handler
        dice_rolls = self.dice.roll_multiple(len(self.players))

        # players order
        starting_player = self.players[dice_rolls.index(max(dice_rolls))]
        self.players = self.players[self.players.index(starting_player):] + self.players[:self.players.index(starting_player)]

        #players color
        self.set_players_color()


    def set_players_color(self):

        for iter, key, value in zip(range(len(self.players)), OFFSETS.keys(), OFFSETS.values()):
            self.players[iter].color = key
            self.players[iter].offset = value


    def setup_game(self):
        self.setup_players()

        for player in self.players:
            for piece in player.pieces:
                self.add_off_board_piece(piece)


    def player_roll_dice(self, player, dice_value = 0):
        # Maybe change dice roll implementation into a gui handler
        dice_value = self.dice.roll()

        # TODO: define usage of on board and off board pieces

        random_piece_position = random.randint(0, len(player.get_pieces_on_board()) - 1)

        if dice_value == 1 or dice_value == 6:
            if len(player.get_pieces_off_board()) > 0:
                self.move_piece_from_off_board_to_on_board(player.get_pieces_off_board()[0], 0)
            else:
                self.move_piece(player.get_pieces_on_board()[random_piece_position], dice_value)
            return True # Player gets another turn
        else:
            # Change implementation, check if player have pieces on board
            if len(player.get_pieces_on_board()) > 0:
                self.move_piece(self.on_board_pieces[random_piece_position], dice_value)
            else:
                print('No pieces on board')
            return False # Player does not get another turn


    def add_off_board_piece(self, piece):
        self.off_board_pieces.append(piece)
        piece.set_off_board_values()

    
    def add_on_board_piece(self, piece, position = 0):
        self.on_board_pieces.append(piece)
        piece.set_on_board_values(position)


    def remove_on_board_piece(self, piece):
        self.on_board_pieces.remove(piece)


    def remove_off_board_piece(self, piece):
        self.off_board_pieces.remove(piece)

    
    def move_piece_from_off_board_to_on_board(self, piece, position):
        self.add_on_board_piece(piece, position)
        self.remove_off_board_piece(piece)


    def move_piece_from_on_board_to_off_board(self, piece):
        self.add_off_board_piece(piece)
        self.remove_on_board_piece(piece)
    

    def move_piece(self, piece, dice_value):
        # TODO: define the logic for moving a piece
        piece.move(dice_value)

        #TODO: define pieces actions like eating other pieces

        # Relative piece position
        piece_position = piece.position
