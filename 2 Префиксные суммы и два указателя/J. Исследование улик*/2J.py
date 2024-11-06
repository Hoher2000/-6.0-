from sys import stdin 

data = stdin.read().splitlines() 

n = int(data[0])
arr = tuple(int(i) for i in data[1].split()[:n])
m, k = map(int, data[2].split())
xlist = tuple(int(i) for i in data[3].split()[:m])

def solve(n, arr, m, k, xlist):

    ans = [0] * (n+1)
    ans[1] = 1
    r = l = n - 1
    kk = k    

    while l != 0:
        if arr[l-1] == arr[l]:
            if not kk:
                ans[r + 1] = l + 1
                while arr[r] != arr[r-1]:
                    r -= 1
                    ans[r+1] = l + 1
                if l == r:
                    r -= 1
                    l = r
                else:
                    r -= 1                    
                kk = min(kk + 1, k)              
            else:
                kk -= 1
                l -= 1
        elif arr[l-1] < arr[l]:
            l -= 1
        else:            
            if r == l:
                ans[r+1] = l+1
                r -= 1
                l = r                
            else:                            
                for ii in range(r, l - 1, -1):
                    ans[ii+1] = l+1
                l -= 1
                r = l
                kk = k     
        #print(l, r, kk)       

    for ii in range(r, l, -1):
        ans[ii+1] = l+1

    res = [0]*m
    for i in range(m):
        res[i] = ans[xlist[i]]
    #print(ans)
    return res

print(*solve(n, arr, m, k, xlist))
