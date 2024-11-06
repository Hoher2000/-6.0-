from sys import stdin
import bisect

data = stdin.read().split()
n, m = map(int, data[:2])
nums = tuple(int(i) for i in data[2:n+2])

cnt = 0
l = 1
for i in range(n):
    ind = bisect.bisect(nums, nums[i]+m, l)
    if ind < n and nums[ind] - nums[i] > m:
        cnt += n - ind
        l = ind
print(cnt)
