from piece import Piece

class Player():
    def __init__(self, name = 'default') -> None:
        self.name = name
        self.on_board_pieces = []
        self.off_board_pieces = []
        
        self.assign_pieces()

    def assign_pieces(self):
        for i in range(4):
            self.off_board_pieces.append(Piece(i + 1))

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    