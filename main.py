import pygame
import time
import random
#uses random for the apples

pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((125, 125, 125))


def p(g):
    print(" " + str(g)[1:][:-1].replace("],", "]\n"))


class SQ:
    sS = []
    eS = []

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
        if self.val == 0:
            pygame.draw.rect(self.screen, (255, 255, 255),
                             pygame.Rect(2.5 + self.x, 2.5 + self.y, 45, 45))
        elif self.val == 1:
            pygame.draw.rect(self.screen, (0, 0, 0),
                             pygame.Rect(2.5 + self.x, 2.5 + self.y, 45, 45))
        elif self. val == 2:
            pygame.draw.rect(self.screen, (255, 125, 125),
                             pygame.Rect(2.5 + self.x, 2.5 + self.y, 45, 45))
    def __repr__(self):
        return str(self.val)
        #return "("+str(self.xd) +","+ str(self.yd)+")"
#Added redraw function
    def redraw(self, v,xd=0,yd=0):

        self.val = v
        if (self.val == 0 and not xd == 2):
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
        
        elif self. val == 2:
            pygame.draw.rect(self.screen, (255, 125, 125),
                             pygame.Rect(2.5 + self.x, 2.5 + self.y, 45, 45))
        

board = [[SQ(j, i, 0, window) for i in range(10)] for j in range(10)]
s = 4
#Different bord set up becuase of redraw
for i in range(2, 5, 1):
    board[s][i]=SQ(s, i, 1, window,1)
board[s][8] = SQ(s,8,2,window,0)


SQ.eS = [s, 2]
SQ.sS = [s, 4]



run = True

xd = 1
yd = 0
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:

            #Fixes Shrinking bug
            if event.key == pygame.K_RIGHT and not  xd == -1:
                xd = 1
                yd = 0
            elif event.key == pygame.K_LEFT and not  xd == 1 :
                xd = -1
                yd = 0
            elif event.key == pygame.K_DOWN and not yd == -1:
                xd = 0
                yd = 1

            elif event.key == pygame.K_UP and not yd == 1:
                xd = 0
                yd = -1
            

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
            board[SQ.sS[0]][SQ.sS[1]].redraw(1,xd,yd)
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


    #four one line if statements for the wrap arround affect
    SQ.sS[0] = -1 if SQ.sS[0]+yd == 10 else SQ.sS[0]
    SQ.sS[1] = -1 if SQ.sS[1]+xd == 10 else SQ.sS[1]
    SQ.eS[0] = 0 if SQ.eS[0] == 10 else SQ.eS[0]
    SQ.eS[1] = 0 if SQ.eS[1] == 10 else SQ.eS[1]
    


    #moves the snake using xd,yd to determine new position

    if board[SQ.sS[0]+yd][SQ.sS[1] + xd].val != 2:
        SQ.eS = board[SQ.eS[0]][SQ.eS[1]].redraw(0)
    #adds more apples
    else:
        rC = 0
        rR = 0
        while not board[rC][rR].val == 0:
            rC = random.randint(1,9)
            rR = random.randint(1,9)
        board[rC][rR].redraw(2)
    

    SQ.sS = board[SQ.sS[0]+yd][SQ.sS[1] + xd].redraw(1,xd,yd)
    
    time.sleep(.2)
    

pygame.quit()
exit()
