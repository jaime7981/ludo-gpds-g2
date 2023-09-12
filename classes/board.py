from classes.dice import Dice

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
    

    def move_piece(self, piece, position):
        piece.position = position
    