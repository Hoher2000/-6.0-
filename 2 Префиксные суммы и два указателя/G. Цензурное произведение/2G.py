from sys import stdin

data = stdin.read().split()
n, c = map(int, data[:2])
s = data[2]
l = r = bestlen = 0
d = {}
grub = 0
while r < n:
    if s[r] != 'b':
        d.setdefault(s[r], 0)
        d[s[r]] += 1
        bestlen = max(r-l, bestlen)
        r += 1
    else:
        if grub + d.get('a', 0) <= c:
            grub += d.get('a', 0)
            d.setdefault('b', 0)
            d['b'] += 1
            bestlen = max(r-l, bestlen)
            r += 1
        else:
            
            while s[l] != 'a':
                if s[l] == 'b':
                    d['b'] = d['b'] - 1 if d['b'] >= 1 else 0
                l += 1    
            d['a'] -= 1
            l += 1
            if 'b' in d:
              if grub >= d['b']:
                  grub -= d['b']
              else:
                  grub = 0



print(bestlen+1)
