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
        
        can_move = self.move_onboard_piece(player, dice_value)

        if can_move == False:
            play_again = True
        
        return play_again
    

    def move_onboard_piece(self, player: Player, dice_value):
        if len(player.get_pieces_on_board()) > 0:
            random_piece_position = random.randint(0, len(player.get_pieces_on_board()) - 1)
            can_move = self.move_piece(player.get_pieces_on_board()[random_piece_position], dice_value)
            return can_move
        else:
            print('No pieces on board')
            return True
    

    def play_turn(self):
        player = self.players[self.turn % len(self.players)]

        dice_value = self.dice.roll()
        print(f'{player.color} rolled {dice_value}')

        player_play_again = self.player_roll_dice(player, dice_value)

        if player_play_again:
            return (dice_value, player)

        self.turn += 1
        if self.turn == len(self.players):
            self.turn = 0

        return (dice_value, player)


    def add_off_board_piece(self, piece: Piece):
        self.off_board_pieces.append(piece)
        piece.set_off_board_values()

    
    def add_on_board_piece(self, piece: Piece):
        self.on_board_pieces.append(piece)
        piece.set_on_board_values(OFFSETS[piece.player.color])

    
    def move_piece_from_off_board_to_on_board(self, piece: Piece):
        self.add_on_board_piece(piece)
        self.off_board_pieces.remove(piece)


    def move_piece_from_on_board_to_off_board(self, piece: Piece):
        self.add_off_board_piece(piece)
        self.on_board_pieces.remove(piece)
    

    def move_piece(self, piece: Piece, dice_value):
        board_piece_position = (OFFSETS[piece.player.color] + piece.position + dice_value) % BOARD_LOOP
        
        can_move = piece.move(dice_value, board_piece_position)

        self.moving_piece_send_opponent_piece_to_off_board(piece)

        print(f'Relative piece position: {piece.position}, Board piece position: {piece.board_position}')

        return can_move


    def piece_is_on_safe_square(self, piece: Piece):
        if piece.position % 13 == 0:
            return True
        
        return False
    

    def pieces_are_on_same_square(self, piece1: Piece, piece2: Piece):
        if piece1.board_position == piece2.board_position:
            return True
        
        return False
    

    def pieces_are_different_color(self, piece1: Piece, piece2: Piece):
        if piece1.player.color != piece2.player.color:
            return True
        
        return False
    

    def moving_piece_send_opponent_piece_to_off_board(self, piece: Piece):
        for player in self.players:
            for player_piece in player.pieces:
                if self.pieces_are_on_same_square(piece, player_piece) and self.pieces_are_different_color(piece, player_piece):
                    # TODO: optional, check if pieces are on safe square
                    self.move_piece_from_on_board_to_off_board(player_piece)
                    return True
        
        return False