

class Piece():
    def __init__(self, piece_number = -1, x = -1, y  = -1) -> None:
        self.piece_number = piece_number
        self.position = [x, y]

        self.on_board = False


    def __str__(self) -> str:
        return str(self.piece_number)
    
    
    def __repr__(self) -> str:
        return str(self.piece_number)