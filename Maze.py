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

allCells=[]
def create_maze():
    for numberX in range(40):
        for numberY in range(24):  
            Cell=node(numberX*20,numberY*20,False,False)
            allCells.append(Cell)
def Get_neibours(Cell):
    Allneigh=[]
    #left neigh
    Left_position=Cell.pX-20
    Right_position=Cell.pX+20
    Top_position=Cell.pY-20
    Bottom_position=Cell.pY+20
    #ignore negative and above 640
    for number in range(40*24):
        if Left_position== allCells[number].pX and Cell.pY== allCells [number].pY:
            Allneigh.append(allCells[number])
        if Right_position== allCells[number].pX and Cell.pY== allCells [number].pY:
            Allneigh.append(allCells[number])
        if Top_position== allCells[number].pY and Cell.pX== allCells [number].pX:
            Allneigh.append(allCells[number])
        if Bottom_position== allCells[number].pY and Cell.pX== allCells [number].pX:
            Allneigh.append(allCells[number])
   
    return (Allneigh)
create_maze()
record=[allCells[0]]
visited_cells=[]
Autoplay=False

current_time=0
next_play_time=0

while True:
    current_time+=0.01
    if current_time>=next_play_time and Autoplay==True:
        next_play_time+=0.001
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
    for number in range(40*24): 
        if allCells[number].wall==True:
            pygame.draw.rect(gamescreen,"Brown",(allCells[number].pX,allCells[number].pY,19,19))
        else:
             pygame.draw.rect(gamescreen,allCells[number].colour,(allCells[number].pX,allCells[number].pY,19,19))
    pygame.display.flip()

    for event in pygame.event.get():

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                Autoplay=True
                print("button pressed")
               
                
                


        if event.type==pygame.QUIT:
            exit()