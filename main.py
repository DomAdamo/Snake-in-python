import pygame

pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((125,125,125))

def p(g):
    print(" "+str(g)[1:][:-1].replace('],',"],\n"))

class Square:

    def __init__(self,c,r,v,w,d=0):
        self.c = c
        self.r = r
        self.val = v
        self.w=w
        self.dir = d
        pygame.draw.rect(self.w, (255, 255, 255), pygame.Rect(2.5+r*50,2.5+ c*50, 45, 45))

    def __repr__(self):
        return str(self.val)

    def changeVal(self,nV):
        self.v = nV
        if nV  == 1:
            pygame.draw.rect(self.w, (0, 0, 0), pygame.Rect(2.5+self.r*50,2.5+ self.c*50, 45, 45))
        else:
            pygame.draw.rect(self.w, (255, 255, 255), pygame.Rect(2.5+self.r*50,2.5+ self.c*50, 45, 45))
    
board= [[Square(j,i,0,window) for i in range(10)]for j in range(10)]
board[4][2].changeVal(1)
board[4][3].changeVal(1)
board[4][4].changeVal(1)

p(board)





vel = 5

run = True
coords= [[4,2],[4,4]]

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))

    
    board[coords[0][0]][coords[0][1]].changeVal(0)
    
    pygame.display.flip()

pygame.quit()


