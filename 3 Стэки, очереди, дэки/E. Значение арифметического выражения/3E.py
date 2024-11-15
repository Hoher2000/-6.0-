from sys import stdin

s = stdin.read().strip()

def solve(postfix):
    if not postfix: return "WRONG"
    stack = []
    length = 0;
    for op in postfix:
        if op == "+":
            stack[length-2] += stack[length-1]
            stack.pop()
            length -= 1
        elif op == "-":
            stack[length-2] -= stack[length-1]
            stack.pop()
            length -= 1
        elif op == "*":
            stack[length-2] *= stack[length-1]
            stack.pop()
            length -= 1
        elif op.isdigit():
            stack.append(int(op))
            length += 1
        else:
            return "WRONG"   
    if stack: return stack.pop()
    return "WRONG" 

def topostfix(s):
    stack, res = [], []
    i = 0
    lenst = 0
    while i != len(s):
        if (i == 0 or s[i-1] == '(' or (i > 1 and s[i-2:i] == "( ")) and s[i] == '-':
            res.append("0");
            stack.append("-")
            lenst += 1
            i += 1
        elif s[i] == ' ':
            i += 1
            continue
        elif s[i].isdigit():
            if s[i-1] == ' ' and s[i-2].isdigit(): return
            digit = ""
            while i != len(s) and s[i].isdigit():
                digit += s[i]
                i += 1
            res.append(digit)
        elif s[i] == '*':
            while (stack and stack[lenst-1] == "*"):
                res.append(stack.pop())
                lenst -= 1
            stack.append("*")
            lenst += 1
            i += 1
        elif s[i] in '+-':
            while stack and stack[lenst-1] in "*-+":
                res.append(stack.pop())
                lenst -= 1
            stack.append(s[i])
            lenst += 1
            i += 1
        elif s[i] == '(':
            stack.append("(")
            lenst += 1
            i += 1
        elif s[i] == ')':
            while stack and stack[-1] != "(":
                res.append(stack.pop())
                lenst -= 1
            if stack:
                stack.pop()
                lenst -= 1
            else: return 
            i += 1
        else:
            return

    while stack:
        res.append(stack.pop())
    #print(res)
    return res

print(solve(topostfix(s)))