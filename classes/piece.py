

class Piece():
    def __init__(self, player = None, piece_number = -1, position = 0) -> None:
        self.player = player
        self.piece_number = piece_number
        self.position = position
        self.board_position = position
        self.on_board = False


    def set_off_board_values(self):
        self.on_board = False
        self.position = 0


    def set_on_board_values(self):
        self.on_board = True
        self.position = 0


    def set_position(self, position):
        self.position = position


    def move(self, number_of_moves, board_position = None):
        self.position += number_of_moves
        self.board_position = board_position


    def __str__(self) -> str:
        return str(self.piece_number)
    
    
    def __repr__(self) -> str:
        return f'Piece(color: {self.player.color}, position: {self.position}, on_board: {self.on_board})'