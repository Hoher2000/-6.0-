from sys import stdin

data = stdin.read().split()
n = int(data[0])
nums = tuple(int(i) for i in data[1:n+1])
s = 0
for i in nums:
    s += i
    print(s, end=' ')
