import pygame
import time
pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((125, 125, 125))


def p(g):
    print(" " + str(g)[1:][:-1].replace("],", "]\n"))


class square:
    def __init__(self,c,r,val,screen,dire=0,):
        self.r = r
        self.c = c
        self.d = dire
        self.x = r * 50
        self.y = c * 50
        self.val = val
        self.screen = screen
        if (self.val != 1):
            pygame.draw.rect(self.screen, (255, 255, 255),
                             pygame.Rect(2.5 + self.x, 2.5 + self.y, 45, 45))
        else:
            pygame.draw.rect(self.screen, (0, 0, 0),
                             pygame.Rect(2.5 + self.x, 2.5 + self.y, 45, 45))

    def __repr__(self):
        return str(self.val)
#Added redraw function
    def redraw(self, v):
        
        self.val = v
        if (self.val != 1):
            pygame.draw.rect(self.screen, (255, 255, 255),
                             pygame.Rect(2.5 + self.x, 2.5 + self.y, 45, 45))
        else:
            pygame.draw.rect(self.screen, (0, 0, 0),
                             pygame.Rect(2.5 + self.x, 2.5 + self.y, 45, 45))

        

board = [[square(j, i, 0, window) for i in range(10)] for j in range(10)]
for i in range(2, 5, 1):
    board[4][i]=square(4, i, 1, window)

coords = [[4, 2], [4, 4]]

p(board)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            pass
    pygame.display.flip()

    #added animation
    time.sleep(20)
    
    board[coords[0][0]][coords[0][1]].redraw(0)
    
pygame.quit()

