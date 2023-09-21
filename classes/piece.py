
END_GAME_OFFSET = {
    'red': 0,
    'green': 6,
    'yellow': 12,
    'blue': 18
}

class Piece():
    def __init__(self, player = None, piece_number = -1, position = 0) -> None:
        self.player = player
        self.piece_number = piece_number
        self.position = position
        self.board_position = position
        self.on_board = False
        self.crown = False


    def set_off_board_values(self):
        self.on_board = False
        self.crown = False
        self.position = 0
        self.board_position = -1


    def set_on_board_values(self, board_position):
        self.on_board = True
        self.position = 0
        self.board_position = board_position


    def set_position(self, position):
        self.position = position

    def move(self, number_of_moves, board_position = None, board_loop = 52):
        
        if self.position > board_loop and self.position < board_loop + 6:
            self.position += number_of_moves
            self.board_position = self.position + END_GAME_OFFSET[self.player.color]
            return True
        elif self.position == board_loop + 6:
            return False
        elif self.position <= board_loop:
            self.position += number_of_moves
            self.board_position = board_position
            return True
        else:
            return False

    def __str__(self) -> str:
        return str(self.piece_number)
    
    
    def __repr__(self) -> str:
        return f'\nPiece(\n color: {self.player.color}\n position: {self.position}\n board_position: {self.board_position}\n on_board: {self.on_board}\n crown: {self.crown})'