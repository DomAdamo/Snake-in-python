import pygame
import time
pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((125,125,125))

def p(g):
    print(" "+str(g)[1:][:-1].replace('],',"],\n"))

class Square:

    def __init__(self,c,r,v,w,xd=0,yd=0):
        self.c = c
        self.r = r
        self.xd = xd
        self.yd = yd
        self.val = v
        self.w=w
        
        pygame.draw.rect(self.w, (255, 255, 255), pygame.Rect(2.5+r*50,2.5+ c*50, 45, 45))

    def __repr__(self):
        return "("+str(self.xd)+","+str(self.yd)+")"

    def redraw(self,nV,xD,yD):
        self.v = nV
        if nV  == 1:
            self.xd = xD
            self.yd = yD
            pygame.draw.rect(self.w, (0, 0, 0), pygame.Rect(2.5+self.r*50,2.5+ self.c*50, 45, 45))
            return [self.c,self.r]
        else:
            YD=self.yd
            XD = self.xd
            self.xd=0
            self.yd = 0
            pygame.draw.rect(self.w, (255, 255, 255), pygame.Rect(2.5+self.r*50,2.5+ self.c*50, 45, 45))
            return [self.c+YD,self.r+XD]

        
board= [[Square(j,i,0,window) for i in range(10)]for j in range(10)]
board[4][2].redraw(1,1,0)
board[4][3].redraw(1,1,0)
board[4][4].redraw(1,1,0)

p(board)





vel = 5

run = True
coords= [[4,2],[4,4]]
xd = 1
yd = 0
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not  xd == -1:
                xd = 1
                yd = 0
            elif event.key == pygame.K_LEFT and not  xd == 1:
                xd = -1
                yd = 0
            elif event.key == pygame.K_DOWN and not yd == -1:
                xd = 0
                yd = 1

            elif event.key == pygame.K_UP and not yd == 1:
                xd = 0
                yd = -1
    board[coords[1][0]][coords[1][1]].redraw(1,xd,yd)
    pygame.display.update()

    time.sleep(.2)
    coords[0] = board[coords[0][0]][coords[0][1]].redraw(0,0,0)
    coords[1] = board[coords[1][0]+yd][coords[1][1]+xd].redraw(1,xd,yd)
    p(board)
    print("\n")
    
pygame.quit()


