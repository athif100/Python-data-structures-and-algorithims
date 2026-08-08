import pygame
import pprint
gamescreen=pygame.display.set_mode((800,480))
class node:
    def __init__(self,pX,pY,wall):
        self.pX=pX
        self.pY=pY
        self.wall=wall
Cell1=node(0,0,False)
Cell2=node(160,0,False)
Cell3=node(320,0,False)  
Cell4=node(480,0,False)
Cell5=node(640,0,False) 
Cell6=node(0,160,False)
Cell7=node(160,160,False)
Cell8=node(320,160,False)  
Cell9=node(480,160,False)
Cell10=node(640,160,False)
Cell11=node(0,320,False)
Cell12=node(160,320,False)
Cell13=node(320,320,False)  
Cell14=node(480,320,False)
Cell15=node(640,320,False)

allCells=[Cell1,Cell2,Cell3,Cell4,Cell5,Cell6,Cell6,Cell7,Cell8,Cell9,Cell10,Cell11,Cell12,Cell13,Cell14,Cell15]
def Get_neibours(Cell):
    Allneigh=[]
    #left neigh
    Left_position=Cell.pX-160
    Right_position=Cell.pX+160
    Top_position=Cell.pY-160
    Bottom_position=Cell.pY+160
    #ignore negative and above 640
    for number in range(16):
        if Left_position== allCells[number].pX:
            Allneigh.append(allCells[number])
        if Right_position== allCells[number].pX:
            Allneigh.append(allCells[number])
        if Top_position== allCells[number].pY:
            Allneigh.append(allCells[number])
        if Bottom_position== allCells[number].pY:
            Allneigh.append(allCells[number])
    pprint.pprint(Allneigh)
Get_neibours(Cell1)
while True:
    for number in range(16):    
        pygame.draw.rect(gamescreen,"Blue",(allCells[number].pX,allCells[number].pY,159,159))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()