import pygame

class GUI():
    def __init__(self, width = 612, height= 612) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.tick = 60
        self.background = pygame.image.load('./assets/board.jpg')


    def run_game(self):
        while self.running:
            self.clock.tick(self.tick)
            self.screen.fill((0, 0, 0))

            self.screen.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()

        pygame.quit()