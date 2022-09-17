# Eric Trinh / 20091235 / game.py

import pygame
import columns

# R: red, G: green, B: blue, Y: yellow, C: cyan, P: purple, H: brown
colors = {' ': (255,255,255),'R': (200,0,0),'G': (0,200,0),'B': (0,0,200),
          'Y': (200,200,0),'C': (0,200,200),'P': (200,0,200),'H':(150,75,0)}


class ColumnsGame:
    def __init__(self):
        self._running = True
        self._columns = columns.Columns()
        
    def run(self):
        pygame.init()
        pygame.display.set_mode((600,600),pygame.RESIZABLE)
        clock1 = pygame.time.Clock()
        clock2 = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT,1000)
        
        while self._running:
            clock1.tick(30)
            if not self._columns._faller_exists():
                self._columns.create_faller()
            self._handle_events()
            self._redraw()
            try:
                if not self._columns._faller_exists():
                    self._columns.is_game_over()
            except:
                self._print_game_over()

        pygame.time.delay(3000)
        pygame.quit()

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
                self._columns.update_status()
            elif event.type == pygame.USEREVENT:
                self._columns.fall_faller()
                self._columns.update_status()
            elif event.type == pygame.KEYDOWN:
                if event.key == 32:
                    self._columns.rotate_faller()
                    self._columns.update_status()
                elif event.key == 1073741904:
                    self._columns.shift_faller(-1)
                    self._columns.update_falling()
                elif event.key == 1073741903:
                    self._columns.shift_faller(1)
                    self._columns.update_falling()

    def _redraw(self):
        surface = pygame.display.get_surface()
        surface.fill(pygame.Color(255,255,255))
        board = self._columns._board
        status = self._columns._status
        delta_x = surface.get_width() / 6
        delta_y = surface.get_height() / 13
        for col in range(6):
            for row in range(13):
                if status[col][row+3] in [0,1]:
                    palette = pygame.Color(colors[board[col][row+3]])
                    rectangle = pygame.Rect(col*delta_x,row*delta_y,delta_x,delta_y)
                    pygame.draw.rect(surface,palette,rectangle)
                elif status[col][row+3] == 2:
                    palette = pygame.Color(colors[board[col][row+3]])
                    rectangle = pygame.Rect(col*delta_x,row*delta_y,delta_x,delta_y)
                    pygame.draw.ellipse(surface,palette,rectangle)
                if status[col][row+3] == 3:
                    palette = list(pygame.Color(colors[board[col][row+3]]))
                    for i in range(3):
                        if palette[i] != 0:
                            palette[i] -= 75
                    rectangle = pygame.Rect(col*delta_x,row*delta_y,delta_x,delta_y)
                    pygame.draw.rect(surface,tuple(palette),rectangle)

        black = pygame.Color(0,0,0)
        for col in range(1,6):
            start = (col*delta_x,0)
            stop = (col*delta_x,surface.get_height())
            pygame.draw.line(surface,black,start,stop,3) 
        for row in range(1,13):
            start = (0,row*delta_y)
            stop = (surface.get_width(),row*delta_y)
            pygame.draw.line(surface,black,start,stop,3) 
        
        pygame.display.flip()

    def _end_game(self):
        self._running = False

    def _print_game_over(self):
        surface = pygame.display.get_surface()
        surface.fill(pygame.Color(255,255,255))
        font = pygame.font.SysFont(None, 60)
        text_image = font.render('GAME OVER', True, pygame.Color(0,0,0))
        surface.blit(text_image, ((surface.get_width()-text_image.get_width())/2,(surface.get_height()-text_image.get_height())/2))
        pygame.display.flip()
        self._running = False


if __name__ == '__main__':
    ColumnsGame().run()
