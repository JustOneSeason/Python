#8.14
def heappush(heap, n) :
    heap.append(n)
    i = len(heap)-1
    while i != 1 :
        pi = i//2 
        if n <= heap[pi]:
            break
        heap[i] = heap[pi]
        i = pi
    heap[i] = n	


# 8.15
def heappop(heap) :
    size = len(heap) - 1
    if size == 0 :
       return None

    root = heap[1]
    last = heap[size]
    pi = 1 
    i = 2 

    while (i <= size):
        if i<size and heap[i] < heap[i+1]:
            i += 1
        if last >= heap[i]:
            break
        heap[pi] = heap[i]
        pi = i              
        i *= 2

    heap[pi] = last
    heap.pop()
    return root

