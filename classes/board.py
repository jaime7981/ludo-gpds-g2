from classes.dice import Dice
from classes.piece import Piece
from classes.player import Player
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
        self.turn = 0

    
    def add_player(self, player: Player):
        if len(self.players) <= 4:
            self.players.append(player)
        
        else:
            print('Max number of players reached')


    def remove_player(self, player: Player):
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


    def player_roll_dice(self, player: Player, dice_value = 0):
        play_again = False

        if dice_value == 1 or dice_value == 6:
            play_again = True

            if len(player.get_pieces_off_board()) > 0:
                self.move_piece_from_off_board_to_on_board(player.get_pieces_off_board()[0])
                return play_again # Player gets another turn
        
        self.move_onboard_piece(player, dice_value)
        
        return play_again
    

    def move_onboard_piece(self, player: Player, dice_value):
        if len(player.get_pieces_on_board()) > 0:
            random_piece_position = random.randint(0, len(player.get_pieces_on_board()) - 1)
            self.move_piece(player.get_pieces_on_board()[random_piece_position], dice_value)
        else:
            print('No pieces on board')
    

    def play_turn(self):
        player = self.players[self.turn % len(self.players)]

        dice_value = self.dice.roll()
        print(f'{player.color} rolled {dice_value}')

        player_play_again = self.player_roll_dice(player, dice_value)

        print(f'On Board Pieces:\n{self.on_board_pieces}\n')

        if player_play_again:
            return (True, dice_value, player)

        self.turn += 1
        if self.turn == len(self.players):
            self.turn = 0

        return (False, dice_value, player)


    def add_off_board_piece(self, piece: Piece):
        self.off_board_pieces.append(piece)
        piece.set_off_board_values(OFFSETS[piece.player.color])

    
    def add_on_board_piece(self, piece: Piece):
        self.on_board_pieces.append(piece)
        piece.set_on_board_values()

    
    def move_piece_from_off_board_to_on_board(self, piece: Piece):
        self.add_on_board_piece(piece)
        self.off_board_pieces.remove(piece)


    def move_piece_from_on_board_to_off_board(self, piece: Piece):
        self.add_off_board_piece(piece)
        self.on_board_pieces.remove(piece)
    

    def move_piece(self, piece: Piece, dice_value):
        board_piece_position = (OFFSETS[piece.player.color] + piece.position + dice_value) % BOARD_LOOP
        
        piece.move(dice_value, board_piece_position)

        print(f'Relative piece position: {piece.position}, Board piece position: {piece.board_position}')
