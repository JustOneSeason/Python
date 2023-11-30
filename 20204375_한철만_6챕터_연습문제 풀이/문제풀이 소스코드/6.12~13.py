class Node:
    def __init__ (self, elem, next=None):
        self.data = elem 
        self.link = next

class LinkedList:
    def __init__( self ):
        self.head = None

    
    def isEmpty( self ): 
        return self.head == None
    def isFull( self ): 
        return False

    def getNode(self, pos) :
        if pos < 0 : 
            return None
        node = self.head
        while pos > 0 and node != None :
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node == None : 
            return None
        else : 
            return node.data

    def insert(self, pos, elem) :
        before = self.getNode(pos-1)
        if before == None :         # 맨 앞에 삽입함
            self.head = Node(elem, self.head)
        else :
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before == None :         # 맨 앞 노드를 삭제
            if self.head is not None :
                self.head = self.head.link
        elif before.link != None :
            before.link = before.link.link
    def printForward(self):
        node = self.head
        while node is not None:
            print(node.data, end=' ')
            node = node.link
    def printReverse(self, node):
        if node is not None:
            self.printReverse(node.link)
            print(node.data, end=' ')    

