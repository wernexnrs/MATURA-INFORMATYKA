def czy_k_podobne(n, A, B, k):
    # A[1..k] = B[n-k+1..n] (tutaj tablice są indeksowane od 0)
    for i in range(k):
        if A[i] != B[n - k + i]:
            return False
    # A[k+1..n] = B[1..n-k]
    for i in range(n - k):
        if B[i] != A[k + i]:
            return False
    return True


def czy_podobne(n, A, B):
    for k in range(n):
        if czy_k_podobne(n, A, B, k):
            return True
    return False


# 1.1 - wiersze 5. i 7. tabeli
print(czy_k_podobne(5, [1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 2))
print(czy_k_podobne(6, [4, 2, 4, 4, 2, 6], [4, 4, 2, 6, 4, 2], 1))
# 1.1 - wiersz 6. tabeli: szukamy k
A = [1, 1, 1, 1, 3, 1, 1, 1, 1]
B = [3, 1, 1, 1, 1, 1, 1, 1, 1]
print([k for k in range(9) if czy_k_podobne(9, A, B, k)])
# 1.3
print(czy_podobne(5, [3, 6, 5, 1, 8], [5, 1, 8, 3, 6]))
