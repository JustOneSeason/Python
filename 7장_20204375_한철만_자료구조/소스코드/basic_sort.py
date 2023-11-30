def printStep(arr, val) :
    print("  Step %2d = " % val, end='')
    print(arr)


# 코드 7.1
def selection_sort(A) :
    n = len(A)
    for i in range(n-1) :
        least = i
        for j in range(i+1, n) :
            if (A[j]<A[least]) :
                least = j
        A[i], A[least] = A[least], A[i]	  
        printStep(A, i + 1);	            

# 코드 7.2
def insertion_sort(A) :
    n = len(A)
    for i in range(1, n) :
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key :
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        printStep(A, i)

# 코드 7.3
def bubble_sort(A) :
    n = len(A)
    for i in range(n-1, 0, -1) :
        bChanged = False
        for j in range (i) :
            if (A[j]>A[j+1]) :
                A[j], A[j+1] = A[j+1], A[j] 
                bChanged = True

        if not bChanged: break
        printStep(A, n - i);	

if __name__ == "__main__":
    org = [ 5, 3, 8, 4, 9, 1, 6, 2, 7 ]

    data = list(org)
    print("Original  :", org)
    selection_sort(data)
    print("Selection :", data)

    data = list(org)
    print("Original  :", org)
    insertion_sort(data)
    print("Insertion :", data)

    data = list(org)
    print("Original  :", org)
    bubble_sort(data)
    print("Bubble    :", data)