from sys import stdin

data = stdin.read().splitlines()

n, b = map(int, data[0].split())
arr = tuple(int(i) for i in data[1].split())

res = 0
size = 0
for i in range(n): 
    #print(size, res)   
    res += size
    res += arr[i]
    size += arr[i]
    size = size - b if b < size else 0
    #print(size, res)
res += size   
print(res)