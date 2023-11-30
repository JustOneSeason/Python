def sum_range(begin, end, step = 1) :
    sum = 0
    for n in range(begin, end, step) :
        sum += n
    return sum

if __name__=="main":
    print("sum", sum_range(1, 9))
    print("sum", sum_range(2, 12,2))