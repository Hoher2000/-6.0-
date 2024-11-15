from sys import stdin

data = stdin.read().splitlines()
d = {'[':']', ']':'[', '(':')', ')':'('}
n = int(data[0])
w, s = data[1], data[2]
l = len(s)
stack = []
stl = 0
for br in s:
    if stack and stack[-1] + br in ['()', '[]']:
        stack.pop()
        stl -= 1
    else:
        stack.append(br)
        stl += 1

while l != n:
    if stack and stack[-1] in '([':
        if n - l - stl + 1 < 3:
            for br in w:
                if stack[-1] + br in '()[]':
                    stack.pop()
                    stl -= 1
                    s += br
                    l += 1
                    break
        else:
            br = min([br for br in d if br in ('[', '(', d[stack[-1]])], key=lambda x: w.index(x))
            if stack[-1] + br in '()[]':
                stack.pop()
                stl -= 1
                s += br
                l += 1
            else:
                stack.append(br)
                stl += 1
                s += br
                l += 1
    else:
        for br in w:
            if br in '([':
                stack.append(br)
                stl += 1
                s += br
                l += 1
                break
    #print(n - l - stl, s, stack)
print(s)