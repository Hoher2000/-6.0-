from sys import stdin

data = stdin.read().split()

n = int(data[0])
nums = tuple(int(i) for i in data[1:n+1])
presums = [0]*(n+1)
for i in range(1, n+1):
    presums[i] = presums[i-1]+nums[i-1]

prepre = [0]*(n)
for i in range(n-2, -1, -1):
    prepre[i] = prepre[i+1]+nums[i]*(presums[n]-presums[i+1])

res = 0
for i in range(n-1):
    res += nums[i]*prepre[i+1]
    


print(res%1000000007)
