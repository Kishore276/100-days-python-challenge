def is_balanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if not stack or stack.pop() != bracket_map[char]:
                return False
    return not stack
print(is_balanced("{[()]}"))
print(is_balanced("{[(])}")) 