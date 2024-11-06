from sys import stdin

data = stdin.read().splitlines() #2 5 3 6 1 4 

n = int(data[0])
a = tuple((int(j), i) for i, j in enumerate(data[1].split()))
b = tuple((int(j), i) for i, j in enumerate(data[2].split()))

inds = tuple(map(int, data[3].split()))

def brute(n, a, b, inds):
    algs = tuple((a[i][0], b[i][0], i) for i in range(n))
    res = [0]*n
    for i in range(n):
        if inds[i]: #max b            
            algs = sorted(algs, key = lambda x: (-x[1], -x[0], x[2]))
            res[i] = algs.pop(0)[2]+1            
        else:
            algs = sorted(algs, key = lambda x: (-x[0], -x[1], x[2]))
            res[i] = algs.pop(0)[2]+1        
    return res

def solve(n, a, b, inds):
    sort_a = sorted(a, key=lambda x: (-x[0], -b[x[1]][0], x[1]))
    sort_b = sorted(b, key=lambda x: (-x[0], -a[x[1]][0], x[1]))
    res = [0]*n
    la = lb = 0
    deleted = set()
    for i in range(n):
        if inds[i]: #max b            
            while sort_b[lb][1] in deleted:
              lb += 1
            res[i] = sort_b[lb][1]+1
            deleted.add(res[i]-1)
            lb += 1            
        else:
            while sort_a[la][1] in deleted:
                la += 1
            res[i] = sort_a[la][1]+1
            deleted.add(res[i]-1)
            la += 1            
    return res
            
print(*solve(n, a, b, inds))
