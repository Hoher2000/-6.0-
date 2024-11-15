from sys import stdin

data = stdin.read().splitlines()

sumstack, stack = [0], []
res = []
for op in data[1:int(data[0])+1]:
    if op[0] == '+':
        sumstack.append(sumstack[-1] + int(op[1:]))
        stack.append(int(op[1:]))
    elif op[0] == '?':
        res.append(sumstack[-1] - sumstack[-int(op[1:])-1])
    else:
        res.append(stack.pop())
        sumstack.pop()
print(*res, sep='\n')      