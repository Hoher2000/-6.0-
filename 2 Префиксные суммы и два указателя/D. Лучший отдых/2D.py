from sys import stdin
import bisect

data = stdin.read().split()
n, m = map(int, data[:2])
nums = sorted(tuple(int(i) for i in data[2:n+2]))
#print(nums)

def days_counter(n,m,nums):
    c = 0
    cnt = 0
    l = 1
    s = set()
    for i in range(n):
        c += 1
        if i in s:
            continue
        #print(i, nums[i])
        cur = i
        ll = l
        help = True
        while (ind := bisect.bisect(nums, nums[cur] + m, ll)) != n:     
            while ind != n and ind in s:
                ind += 1     
            if ind == n: break  
            if help:
                l = ind + 1
            #print('i', i, 'ind', ind, nums[i], nums[ind])
            s.add(ind)
            cur = ind
            ll = ind + 1
            help = False
            c += 1
        cnt += 1
    #print('c', c)
    return cnt     
