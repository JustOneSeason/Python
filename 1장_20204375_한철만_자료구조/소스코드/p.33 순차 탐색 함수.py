def search(A, key) :
    n = len(A)
    for i in range(n) :
        if A[i] == key :
            return i
        
    return -1
