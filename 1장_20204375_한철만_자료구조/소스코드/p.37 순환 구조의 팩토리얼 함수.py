def factorial(n) :
    if n == 1 :
        return 1
    else :
        return n * factorial(n-1)
    
n = 6
print("순환 Factorial %d!" %n, factorial(n))
n = 7
print("순환 Factorial %d!" %n, factorial(n))
n = 9
print("순환 Factorral %d" %n, factorial(n))
