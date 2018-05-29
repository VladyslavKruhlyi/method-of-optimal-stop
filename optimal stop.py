import numpy

N = int(input("The number of applicants: "))
M = int(input("Number of iterations: "))
delta = int(input("Delta: "))


def result(N, delta):
    X = []
    for _ in range(N):
        X.append(numpy.random.randint(160, 190))
    X_max = max(X)
    j = int(N/2.71828) + 1
    x = X[0:j]
    x_max = max(x)
    win = 0
    for i in range(j, N):
        if X[i] > x_max:
            if abs(X_max - X[i]) <= delta or abs(X_max-X[N-1]) <= delta:
                win = 1
            break
        continue
    return win


def res(M):
    win1 = 0
    for _ in range(M):
        if result(N, delta) == 1:
            win1 += 1
    return (print("Probability:" ,win1/M))

res(M)







