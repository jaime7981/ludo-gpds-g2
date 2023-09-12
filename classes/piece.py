

class Piece():
    def __init__(self, player = None, piece_number = -1, position = 0) -> None:
        self.player = player
        self.piece_number = piece_number
        self.position = position
        self.on_board = False


    def set_off_board_values(self):
        self.on_board = False
        self.position = 0


    def set_on_board_values(self, position):
        self.on_board = True
        self.position = position


    def set_position(self, position):
        self.position = position


    def move(self, number_of_moves):
        self.position += number_of_moves


    def __str__(self) -> str:
        return str(self.piece_number)
    
    
    def __repr__(self) -> str:
        return f'Piece({self.player.color}: {self.piece_number}, {self.position}, on_board: {self.on_board})'