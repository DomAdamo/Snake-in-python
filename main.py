import pygame
import time
pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((125, 125, 125))


def p(g):
    print(" " + str(g)[1:][:-1].replace("],", "]\n"))


class square:
    def __init__(self,c,r,val,screen,xd=0,yd=0):
        self.r = r
        self.c = c
        #implements two sets of direction so that not confusing
        self.xd = xd
        self.yd = yd
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
        return "("+str(self.xd) +","+ str(self.yd)+")"
#Added redraw function
    def redraw(self, v,xd=0,yd=0):

        self.val = v
        if (self.val == 0):
            # uses different variables to return, and set 0 so that direction is not stored
            xD = self.xd 
            self.xd = 0
            yD = self.yd
            self.yd = 0
            pygame.draw.rect(self.screen, (255, 255, 255),
                             pygame.Rect(2.5 + self.x, 2.5 + self.y, 45, 45))
            return [self.c + yD,self.r+xD]

        elif self.val== 1:
            #Only sets the direction if it is a new block
            self.xd = xd
            self.yd = yd
            pygame.draw.rect(self.screen, (0, 0, 0),
                             pygame.Rect(2.5 + self.x, 2.5 + self.y, 45, 45))
            return [self.c,self.r]
        

board = [[square(j, i, 0, window) for i in range(10)] for j in range(10)]
s = 4
#Different bord set up becuase of redraw
for i in range(2, 5, 1):
    board[s][i]=square(s, i, 1, window,1)

coords = [[s, 2], [s, 4]]

p(board)

run = True
s = 0
xd = 1
yd = 0
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            s=1
            keys = pygame.key.get_pressed()
            #used to set the direction of the snake
            xd = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]
            yd = keys[pygame.K_DOWN] - keys[pygame.K_UP]

            #Used only to redraw the current block and change its direction for turns
            ## EX ( xd,yd) or each block:
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (1,0), (1,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,1), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]

            #Vs
            board[coords[1][0]][coords[1][1]].redraw(1,xd,yd)
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (1,0), (0,1), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,1), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]
             # [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]

    pygame.display.flip()

    #added animation
    time.sleep(.3)

    #troubleshooting
    print (str(xd) +","+str(yd))
    print(coords)
    p(board)


    #moves the snake using xd,yd to determine new position
    coords[0] = board[coords[0][0]][coords[0][1]].redraw(0)
    coords[1] = board[coords[1][0]+yd][coords[1][1] + xd].redraw(1,xd,yd)

    

pygame.quit()
exit()
