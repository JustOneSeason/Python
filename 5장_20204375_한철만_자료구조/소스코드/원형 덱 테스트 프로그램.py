from CircularDeque import *

dq = CircularDeque()

for i in range(9):
    if i%2==0 : dq.addRear(i)
    else : dq.addFront(i)
print("홀수->전단, 짝수->후단:",dq)

for i in range(2):
    dq.deleteFront()
for i in range(3):
    dq.deletRear()
print("전단삭제x2 후단삭제x3:",dq)

for i in range(9,14):
    dq.addFront(i)
print("전답삽입 9,10,11,12,13",dq)