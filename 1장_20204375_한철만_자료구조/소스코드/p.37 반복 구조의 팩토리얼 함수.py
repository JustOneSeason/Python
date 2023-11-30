def factorial_iter(n) :
    result = 1
    for k in range(1, n+1) :
        result = result * k
    
    return result

n = 5
print('반복 Factorial %d! ='%n, factorial_iter(n))
n = 7
print('반복 Factorial %d! ='%n, factorial_iter(n))
n = 10
print('반복 Factorial %d! ='%n, factorial_iter(n))