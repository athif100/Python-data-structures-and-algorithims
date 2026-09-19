#Record=[two]
#while(length(Record)>0)
#print(Record[0].data)
#if Record [0].left
#save left to record
#if Record [0].right
#save right to record
#[two,three,four]
#delete record[00]
class node:
    def __init__(self,left,right,data):
        self.left=left
        self.right=right
        self.data=data
two=node(None,None,2)
three=node(None,None,3)
four=node(None,None,4)
five=node(None,None,5)
six=node(None,None,6)
seven=node(None,None,7)
eight=node(None,None,8)
two.left=three
two.right=four
three.left=five
three.right=six
four.right=seven
four.left=eight
print(two.left.right.data)
#Breathfirstsearch
Record=[two]
while len(Record)>0:
    print (Record[0].data)
    if Record[0].left:
        Record.append(Record[0].left)
    if Record [0].right:
        Record.append(Record[0].right)
    del Record[0]


