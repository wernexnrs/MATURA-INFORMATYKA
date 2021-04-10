n = 3
k = 0

A = [5, 7, 9]
B = [5, 7, 9]


def czy_k_podobne(n, A, B, k):
    for i in range(k):

        if A[i] != B[n - k + i]:
            return False

    for i in range(n - k):
        if B[i] != A[k + i]:
            return False
    return True


def czy_podobne(n, A, B):
    for k in range(n):
        if czy_k_podobne(n, A, B, k):
            return True
        return False


print(czy_k_podobne(n, A, B, k))
