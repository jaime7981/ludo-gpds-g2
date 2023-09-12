from classes.piece import Piece

class Player():
    def __init__(self, name = 'default', color = 'red', offset = 0) -> None:
        self.name = name
        self.pieces = []
        self.color = color
        self.offset = offset
        
        self.assign_pieces()


    def assign_pieces(self):
        for i in range(4):
            self.pieces.append(Piece(self, i))


    def get_piece(self, piece_number):
        for piece in self.pieces:
            if piece.piece_number == piece_number:
                return piece
        
        return None

    
    def get_pieces(self):     
        return self.pieces
    

    def get_pieces_on_board(self):
        pieces_on_board = []

        for piece in self.pieces:
            if piece.on_board:
                pieces_on_board.append(piece)
        
        return pieces_on_board
    

    def get_pieces_off_board(self):
        pieces_off_board = []

        for piece in self.pieces:
            if not piece.on_board:
                pieces_off_board.append(piece)
        
        return pieces_off_board


    def move_piece_by_number(self, piece_number, number_of_moves):
        piece = self.get_piece(piece_number)
        piece.move(number_of_moves)


    def __str__(self) -> str:
        return self.name
    

    def __repr__(self) -> str:
        return self.name
    