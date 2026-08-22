import pygame
import pprint
import time
gamescreen=pygame.display.set_mode((800,480))
class node:
    def __init__(self,pX,pY,wall,End):
        self.pX=pX
        self.pY=pY
        self.wall=wall
        self.End=End
        self.colour="Blue"
Cell1=node(0,0,False,False)
Cell2=node(160,0,False,False)
Cell3=node(320,0,False,False)  
Cell4=node(480,0,True,False)
Cell5=node(640,0,False,False) 
Cell6=node(0,160,False,False)
Cell7=node(160,160,False,False)
Cell8=node(320,160,True,False)  
Cell9=node(480,160,False,False)
Cell10=node(640,160,False,False)
Cell11=node(0,320,False,False)
Cell12=node(160,320,False,False)
Cell13=node(320,320,False,False)  
Cell14=node(480,320,False,False)
Cell15=node(640,320,False,True)
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
        if Left_position== allCells[number].pX and Cell.pY== allCells [number].pY:
            Allneigh.append(allCells[number])
        if Right_position== allCells[number].pX and Cell.pY== allCells [number].pY:
            Allneigh.append(allCells[number])
        if Top_position== allCells[number].pY and Cell.pX== allCells [number].pX:
            Allneigh.append(allCells[number])
        if Bottom_position== allCells[number].pY and Cell.pX== allCells [number].pX:
            Allneigh.append(allCells[number])
    pprint.pprint(Allneigh)
    return (Allneigh)
Get_neibours(Cell6)
record=[Cell1,]
visited_cells=[]

while True:
   
    for number in range(16): 
        if allCells[number].wall==True:
            pygame.draw.rect(gamescreen,"Brown",(allCells[number].pX,allCells[number].pY,159,159))
        else:
             pygame.draw.rect(gamescreen,allCells[number].colour,(allCells[number].pX,allCells[number].pY,159,159))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                print("button pressed")
                record[0].colour="Green"
                visited_cells.append(record[0])
                if record[0].End==True:
                    print("Maze sloved")
                else:
                    allneigh=Get_neibours(record[0])
                    for number in range(len(allneigh)):
                        if allneigh[number]  in visited_cells:
                            pass
                        else:
                            if allneigh [number].wall==False:
                                
                                record.append(allneigh[number])
                    del record[0]
                
                


        if event.type==pygame.QUIT:
            exit()