def merge_sorted_lists(A, B):

    C = []
    
    i, j = 0, 0
    
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    while i < len(A):
        C.append(A[i])
        i += 1
    while j < len(B):
        C.append(B[j])
        j += 1

    return C

A = input("첫 번째 리스트를 입력하세요 (숫자 사이에 공백을 두고 입력): ").split()
A = [int(x) for x in A]

B = input("두 번째 리스트를 입력하세요 (숫자 사이에 공백을 두고 입력): ").split()
B = [int(x) for x in B]

A.sort()
B.sort()

C = merge_sorted_lists(A, B)

print("두 리스트를 병합한 정렬된 리스트:", C)

