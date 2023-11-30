def number_iter(n) :
    sum = 0
    for i in range(1, n+1) :
       sum = sum + i
    return sum

def number_recur(n) :
    sum = 0
    if n == 1 :
        return 1
    else :
        return n + number_recur(n-1)
    
print("1~10까지의 합(반복) =", number_iter(10))
print("1~10까지의 합(순환) =", number_recur(10))

