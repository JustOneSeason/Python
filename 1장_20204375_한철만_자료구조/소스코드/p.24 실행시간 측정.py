import time

def contains(bag, e) :
    return e in bag

def insert(bag, e) :
    bag.append(e)

def remove(bag, e) :
    bag.remove(e)

def count(bag) :
    return len(bag)


myBag = []

start = time.time()
insert(myBag,'휴대폰')
insert(myBag,'지갑')
insert(myBag,'손수건')
insert(myBag,'빗')
insert(myBag,'자료구조')
insert(myBag,'야구공')
...
end = time.time()
print("실행시간 = ", end-start)