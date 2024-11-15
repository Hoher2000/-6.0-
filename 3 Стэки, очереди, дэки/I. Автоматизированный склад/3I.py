from sys import stdin


data = stdin.read().splitlines()

n = int(data[0])
a, b = map(int, data[1].split())
pd = {}
if abs(a - b) == 2:
    pd[a] = 0
    pd[b] = 0
    for i in range(1, 5):
        pd.setdefault(i, 1)
else:
    if (min(a,b), max(a,b)) == (1, 2):
        pd[min(a,b)] = 0
        pd[max(a,b)] = 1
        pd[min(a,b)+2] = 2
        pd[max(a,b)+2] = 3
    elif (min(a,b), max(a,b)) == (2, 3):
        pd[min(a,b)] = 0
        pd[max(a,b)] = 1
        pd[min(a,b)+2] = 2
        pd[max(a,b)-2] = 3
    elif (min(a,b), max(a,b)) == (3, 4):
        pd[min(a,b)] = 0
        pd[max(a,b)] = 1
        pd[min(a,b)-2] = 2
        pd[max(a,b)-2] = 3
    else:
        pd[max(a,b)] = 0
        pd[min(a,b)] = 1
        pd[max(a,b)-2] = 2
        pd[min(a,b)+2] = 3

deq = [[], [], [], []]
rovers = [[0,0,0,0]] * (n+1)
for k, i in enumerate(data[2:n+2], 1):
    dir, time = map(int, i.split())  
    rovers[k] = [time, pd[dir], time, k, dir]

rovers.sort()

for rover in rovers[1:]:
    deq[rover[4]-1].append(rover)

res = [0] * n
time = 0
while sum([bool(i) for i in deq]):
    now = sorted(d[0] for d in deq if d)
    #print(now)
    if len(now) >= 2 and now[0][0] == now[1][0] and abs(now[0][4] - now[1][4]) == 2 and pd[now[0][4]] == pd[now[1][4]]:# == 0 or (len([k for k in now if k[0] == now[0][0]]) == 2)):
        first = deq[now[0][4]-1].pop(0)
        second = deq[now[1][4]-1].pop(0)
        res[second[3]-1] = second[0]
        res[first[3]-1] = first[0]
        time = first[0] + 1
        for d in deq:
            if d and d[0][0] < time: d[0][0] = time  
        #print(res)      
        continue
    first = deq[now[0][4]-1].pop(0)
    res[first[3]-1] = first[0]
    time = first[0] + 1
    for d in deq:
        if d and d[0][0] < time: d[0][0] = time      
print(*res, sep='\n')  