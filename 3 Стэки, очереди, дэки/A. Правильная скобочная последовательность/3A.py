s =input()

def check(s):
    st = []
    for char in s:
        if char in '([{':
            st.append(char)
            continue
        if not st: return False
        if st[-1] + char in '()[]{}': st.pop()    
        else: return False
    return st == []

print(('no', 'yes')[check(s)])