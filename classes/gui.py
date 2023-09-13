import pygame
from classes.piece import Piece
from classes.board import Board
from classes.player import Player

NUMBER_OF_SQUARES_WIDTH = 15
NUMBER_OF_SQUARES_HEIGHT = 15

ASSETS_PATH = './assets/'

ASSETS_IMAGES = {
    'board': ASSETS_PATH + 'board.jpg',
    'red_piece': ASSETS_PATH + 'red_piece.png',
    'green_piece': ASSETS_PATH + 'green_piece.png',
    'blue_piece': ASSETS_PATH + 'blue_piece.png',
    'yellow_piece': ASSETS_PATH + 'yellow_piece.png',
    'dice_1': ASSETS_PATH + 'dice_1.png',
    'dice_2': ASSETS_PATH + 'dice_2.png',
    'dice_3': ASSETS_PATH + 'dice_3.png',
    'dice_4': ASSETS_PATH + 'dice_4.png',
    'dice_5': ASSETS_PATH + 'dice_5.png',
    'dice_6': ASSETS_PATH + 'dice_6.png',
}

class GUI():
    def __init__(self, width = 612, height= 612) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.square_dimentions = self.setup_square_dimentions()
        self.clock = pygame.time.Clock()
        self.running = True
        self.tick = 60

        self.board = Board()

        loaded_background = pygame.image.load('./assets/board.jpg')
        self.background = pygame.transform.scale(loaded_background, (width, height))


    def setup_board(self):
        self.board.add_player(Player('Player 1', 'red'))
        self.board.add_player(Player('Player 2', 'green'))
        self.board.add_player(Player('Player 3', 'yellow'))
        self.board.add_player(Player('Player 4', 'blue'))

        self.board.setup_game()

    def setup_square_dimentions(self):
        # setup the dimentions of the board based on the screen size
        board_width = self.screen.get_width()
        board_height = self.screen.get_height()

        # setup the dimentions of the squares based on the board size
        square_width = board_width / NUMBER_OF_SQUARES_WIDTH
        square_height = board_height / NUMBER_OF_SQUARES_HEIGHT

        return (square_width, square_height)


    def get_square_center(self, square_x = 0, square_y = 0):
        square_center_x = (square_x * self.square_dimentions[0]) + (self.square_dimentions[0] / 2)
        square_center_y = (square_y * self.square_dimentions[1]) + (self.square_dimentions[1] / 2)

        return (square_center_x, square_center_y)
    

    def draw_image_on_square_center(self, element, square_x = 0, square_y = 0):
        square_center = self.get_square_center(square_x, square_y)
        element_center = (square_center[0] - (element.get_width() / 2), square_center[1] - (element.get_height() / 2))
        self.screen.blit(element, element_center)
    

    def draw_piece(self, piece: Piece, square_x = 0, square_y = 0):
        piece_color = piece.player.color
        # self.draw_element_on_square_center(piece.image, square_x, square_y)
        pygame.draw.circle(self.screen, piece_color, self.get_square_center(square_x, square_y), (self.square_dimentions[0] / 2) - 2)
    

    def draw_pieces(self):
        for player in self.board.players:
            for piece in player.pieces:
                if piece.on_board:
                    # TODO: Make a way to parse the position of the piece to the gui
                    # self.draw_piece(piece, piece.position[0], piece.position[1])
                    
                    pass
    

    def run_game(self):
        self.setup_board()

        while self.running:
            self.clock.tick(self.tick)
            self.screen.fill((0, 0, 0))

            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    self.board.play_turn()

                    #if event.key == pygame.K_RETURN:
                    #    self.board.play_turn()

            pygame.display.update()

        pygame.quit()