from ArraySet import ArraySet

setA = ArraySet()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
print('Set A: ',setA)

setB = ArraySet()
setB.insert('빗')
setB.insert('파이썬 자료구조')
setB.insert('야구공')
setB.insert('지갑')
print("Set B: ", setB)

setA.insert('손수건')
setA.insert('발수건')
print('Set A: ',setA)
setB.insert('빗')
print("Set B: ", setB)

print('A U B :', setA.union(setB))
print('A ^ B :', setA.intersect(setB))
print('A - B :', setA.difference(setB))