from classes.piece import Piece

class Player():
    def __init__(self, name = 'default', color = 'white') -> None:
        self.name = name
        self.pieces = []
        self.color = color
        
        self.assign_pieces()


    def assign_pieces(self):
        for i in range(4):
            self.pieces.append(Piece(i))


    def get_piece(self, piece_number):
        for piece in self.pieces:
            if piece.piece_number == piece_number:
                return piece
        
        return None

    
    def get_pieces(self):     
        return self.pieces


    def move_piece(self, piece_number, x, y):
        piece = self.get_piece(piece_number)
        piece.move(x, y)


    def __str__(self) -> str:
        return self.name
    

    def __repr__(self) -> str:
        return self.name
    