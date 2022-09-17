import pygame




def run() -> None:
    pygame.init()

    try:
        surface = pygame.display.set_mode((600, 600),pygame.RESIZABLE)
        font = pygame.font.SysFont(None, 24)
        clock = pygame.time.Clock()

        running = True  

        while running:
            clock.tick(30)
##            pygame.time.set_timer(pygame.MOUSEBUTTONDOWN,7000)

            
            for event in pygame.event.get():
                pygame.time.set_timer(pygame.USEREVENT,1000)
                print(event)
##                pygame.time.set_timer(event.type,7000)
                if event.type == pygame.QUIT:
                    self._end_game()

            
            
            pygame.display.flip()

    finally:
        pygame.quit()


if __name__ == '__main__':
    run()
