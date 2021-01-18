def insertionSort(A): 
    for i in range(1, len(A)):
        liczba = A[i]

        while i > 0 and A[i - 1] > liczba:
            A[i] = A[i -1]
            i -=1
        A[i] = liczba
    return A
  
arr = [12, 11, 13, 5, 6]

print(insertionSort(arr))
