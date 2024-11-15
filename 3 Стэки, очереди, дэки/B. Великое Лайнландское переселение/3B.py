from sys import stdin

data = stdin.readlines() #-1 4 3 4 -1 6 9 8 9 -1

n = int(data[0])
towns = tuple(int(i) for i in data[1].split())
st = []
ans = [0] * n
for i, cost in enumerate(towns):
    if not st: st.append((i, cost))
    while st and cost < st[-1][1]:
        ans[st[-1][0]] = i
        st.pop()
    st.append((i, cost))
while st:
    ans[st[-1][0]] = -1
    st.pop()

print(*ans)