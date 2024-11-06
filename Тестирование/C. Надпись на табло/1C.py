from sys import stdin

T = lambda arr: list(zip(*arr))

def del_dupl(arr):
    res = []
    for line in arr:
        if not res:
            res.append(line)
        elif line != res[-1]: 
            res.append(line)
    if res and '#' not in res[0]: del res[0]
    if res and '#' not in res[-1]: del res[-1]
    return res        

def scan(tab):
    ops = [del_dupl, T] * 2
    [tab := op(tab) for op in ops]
    templates = [
        [('#',)],    #I

        [('#','#','#'),
         ('#','.','#'),
         ('#','#','#')], #O

        [('#','#'),
         ('#','.'),
         ('#','#')], #C

        [('#','.'),
         ('#','#')], #L

        [('#','.','#'),
         ('#','#','#'),
         ('#','.','#')], #H

        [('#','#','#'),
         ('#','.','#'),
         ('#','#','#'),
         ('#','.','.')], #P
        ]
    answers = 'IOCLHP'
    try:
        return answers[templates.index(tab)]
    except:
        return 'X'
    
data = stdin.read().split()
n = int(data[0])
tab = [tuple(line) for line in data[1:]]
print(scan(tab))
