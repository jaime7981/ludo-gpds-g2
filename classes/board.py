from classes.dice import Dice
import random

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

    
    def set_player_order(self):
        players_roll_for_turns = self.dice.roll_multiple(len(self.players))

        for i in range(len(players_roll_for_turns)):
            for j in range(len(players_roll_for_turns)):
                if players_roll_for_turns[i] > players_roll_for_turns[j]:
                    temp = players_roll_for_turns[i]
                    players_roll_for_turns[i] = players_roll_for_turns[j]
                    players_roll_for_turns[j] = temp

                    temp = self.players[i]
                    self.players[i] = self.players[j]
                    self.players[j] = temp


    def player_roll_dice(self, player):
        dice_value = self.dice.roll()

        if dice_value == 1 or dice_value == 6:
            if len(player.off_board_pieces) > 0:
                self.move_piece_from_off_board_to_on_board(player.off_board_pieces[0], [0, 0])
            else:
                self.move_piece(player.on_board_pieces[0], dice_value)
            self.player_roll_dice(player)
        else:
            if len(player.on_board_pieces) > 0:
                random_piece_position = random.randint(0, len(player.on_board_pieces) - 1)
                self.move_piece(player.on_board_pieces[random_piece_position], dice_value)
            else:
                print('No pieces on board')


    def add_off_board_piece(self, piece):
        self.off_board_pieces.append(piece)

    
    def add_on_board_piece(self, piece, position = [0, 0]):
        self.on_board_pieces.append(piece)
        piece.position = position


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
        piece.position[0] += dice_value

        #TODO: define pieces actions like eating other pieces
    