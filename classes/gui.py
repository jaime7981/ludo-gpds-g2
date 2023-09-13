import pygame
from classes.piece import Piece
from classes.board import Board
from classes.player import Player

NUMBER_OF_SQUARES_WIDTH = 15
NUMBER_OF_SQUARES_HEIGHT = 15

ASSETS_PATH = './assets/'

ASSETS_IMAGES = {
    'board': ASSETS_PATH + 'board.jpg',
    'dice_1': ASSETS_PATH + 'dice_1.png',
    'dice_2': ASSETS_PATH + 'dice_2.png',
    'dice_3': ASSETS_PATH + 'dice_3.png',
    'dice_4': ASSETS_PATH + 'dice_4.png',
    'dice_5': ASSETS_PATH + 'dice_5.png',
    'dice_6': ASSETS_PATH + 'dice_6.png',
}

BOARD_MAP_PATH = ASSETS_PATH + 'board_map.csv'

class GUI():
    def __init__(self, width = 612, height= 612) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.square_dimentions = self.setup_square_dimentions()
        self.clock = pygame.time.Clock()
        self.running = True
        self.tick = 60

        self.board_map = self.load_board_map()
        self.board = Board()

        self.last_dice_value = 1
        self.last_player = None

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
    

    def load_board_map(self):
        board_map = []
        with open(BOARD_MAP_PATH, 'r') as file:
            for line in file:
                board_map.append([int(value) for value in line.split(',')])

        return board_map


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
        pygame.draw.circle(self.screen, piece_color, self.get_square_center(square_x, square_y), (self.square_dimentions[0] / 3))
        pygame.draw.circle(self.screen, (0, 0, 0), self.get_square_center(square_x, square_y), (self.square_dimentions[0] / 3), 3)


    def get_piece_position_from_board_map(self, piece: Piece):
        for y, line in enumerate(self.board_map):
            for x, square in enumerate(line):
                if square == piece.board_position:
                    return (x, y)


    def draw_pieces(self):
        for player in self.board.players:
            for piece in player.pieces:
                if piece.on_board:
                    piece_position = self.get_piece_position_from_board_map(piece)
                    self.draw_piece(piece, piece_position[0], piece_position[1])
    

    def draw_off_board_pieces(self):
        for player in self.board.players:
            number_of_off_board_pieces = 0

            for piece in player.pieces:
                if not piece.on_board:
                    if player.color == 'red':
                        self.draw_piece(piece, 1 + (1 * number_of_off_board_pieces), 1 - (-1 * number_of_off_board_pieces))
                    elif player.color == 'green':
                        self.draw_piece(piece, NUMBER_OF_SQUARES_WIDTH - 2 - (1 * number_of_off_board_pieces), 1 - (-1 * number_of_off_board_pieces))
                    elif player.color == 'yellow':
                        self.draw_piece(piece, NUMBER_OF_SQUARES_WIDTH - 2 - (1 * number_of_off_board_pieces), NUMBER_OF_SQUARES_HEIGHT - 2 + (-1 * number_of_off_board_pieces))
                    elif player.color == 'blue':
                        self.draw_piece(piece, 1 + (1 * number_of_off_board_pieces), NUMBER_OF_SQUARES_HEIGHT - 2 + (-1 * number_of_off_board_pieces))
                
                    number_of_off_board_pieces += 1


    def draw_dice(self):
        dice_image = pygame.image.load(ASSETS_IMAGES[f'dice_{self.last_dice_value}'])
        dice_image = pygame.transform.scale(dice_image, (100, 100))
        
        if self.last_player:
            dice_image.fill(self.last_player.color, special_flags=pygame.BLEND_ADD)
        
        self.draw_image_on_square_center(dice_image, 7, 7)


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
                    play_again, dice_value, player = self.board.play_turn()
                    self.last_dice_value = dice_value
                    self.last_player = player

            self.draw_pieces()
            self.draw_off_board_pieces()
            self.draw_dice()
            pygame.display.update()

        pygame.quit()