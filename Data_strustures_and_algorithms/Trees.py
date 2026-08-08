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
two.left=three
two.right=four
three.left=five
three.right=six
print(two.left.right.data)

        
