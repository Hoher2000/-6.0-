import random

data = stdin.read().split()

n = int(data[0])
arr = tuple(int(i) for i in data[1:n+1])

def brute(n, arr):
    res = [0]*n
    for i in range(n):
        c = 0
        for j in range(n):
            if i != j:
                c += abs(i-j)*arr[j]
        res[i] += c
    #print(res)
    return min(res)

def solve(n, arr):
    pre = [0]*(n+1)
    for i in range(1, n+1):
        pre[i] += pre[i-1]+arr[i-1]
    max = sum(arr[i]*i for i in range(1, n))
    sums = [0]*n
    sums[0] = max
    #print(max)
    for i in range(1,n):
        sums[i] = sums[i-1]-(pre[n]-pre[i])+pre[i]
    return min(sums)

def test():
    for i in range(100):
        n = 10
        arr = [random.randint(1, 20) for i in range(n)]
        if brute(n, arr)!=solve(n, arr): print(n, arr)

print(solve(n, arr))
