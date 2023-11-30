class Car :
    def __init__(self,color,speed = 0):
        self.color = color
        self.speed = speed
    
    def speedUp(self) :
        self.speed += 10

    def speedDown(self) :
        self.speed -= 10
