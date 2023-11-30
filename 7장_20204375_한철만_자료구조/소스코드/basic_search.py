# 코드 7.7
def sequential_search(A, key, low, high) :
    for i in range(low, high+1) : 
        print(A[i], end=' ')
        if A[i] == key :		
            return i				
    return -1				

if __name__ == "__main__":
    array = [ 2, 6, 11, 13, 18, 20, 22, 27, 29, 30, 34, 38, 41, 42, 45, 47 ]
    n = len(array)

    print("입력배열 = ", array)
    key = 34
    print("순차탐색 %d: "%key, sequential_search(array, key, 0, n-1))
 
    key = 23
    print("순차탐색 %d: "%key, sequential_search(array, key, 0, n-1))
