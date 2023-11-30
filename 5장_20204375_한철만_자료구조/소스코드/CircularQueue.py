class CircularQueue :
    def __init__( self, capacity = 8 ) :
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty( self ) :
        return self.front == self.rear
    
    def isFull( self ):
        return self.front == (self.rear+1)%self.capacity
    
    def enqueue( self, item):
        if not self.isFull():
            self.rear = (self.rear + 1)%self.capacity
            self.array[self.rear] = item
        else : pass

    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front +1)%self.capacity
            return self.array[self.front]
        else: pass

    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front+1)%self.capacity]
        else : pass
 #코드 5.2 큐의 전체 요소의 수 계산
    def size( self ):
        return(self.rear - self.front + self.capacity)%self.capacity
 #코드 5.3 문자열 변환을 위한 Str 연산자 중복
    def __str__ ( self ):
        if self.front < self.rear :
            return str(self.array[self.front+1 : self.rear+1])
        else :
            return str(self.array[self.front+1:self.capacity]+\
                       self.array[0:self.rear+1])  
        
    
