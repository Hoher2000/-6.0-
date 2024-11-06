from sys import stdin
import bisect

data = stdin.read().split()
n, m = map(int, data[:2])
nums = tuple(int(i) for i in data[2:n+2])
presums = [0] * (n + 1)

for i in range(1, n + 1):
    presums[i] += presums[i-1] + nums[i-1]

cnt = l = 0
for i in range(n+1):
    ind = bisect.bisect_left(presums, presums[i]+m, l)
    if ind < n+1 and presums[ind] - presums[i] == m:
        cnt += 1
        l = ind
print(cnt)
