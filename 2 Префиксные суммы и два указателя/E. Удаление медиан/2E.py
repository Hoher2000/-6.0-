from sys import stdin

data = stdin.read().split()

n = int(data[0])
nums = sorted(int(i) for i in data[1:n+1])
mid = n // 2 if n % 2 else n // 2 - 1
res = [0]*n
l, r = mid-1, mid+1
res[0] = nums[mid]
i = 1
while l >= 0 and r < n:
    if (n-i) % 2:
        res[i] = nums[r]
        r += 1
    else:
        res[i] = nums[l]
        l -= 1
    i += 1

if l >= 0:
    for j in range(0, l+1):
        res[i] = nums[j]
        i += 1
else:
    for j in range(r, n):
        res[i] = nums[j]
        i += 1
print(*res)
