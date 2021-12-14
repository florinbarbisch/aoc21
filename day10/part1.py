bracket_map = { "(": ")", "[": "]", "{": "}", "<": ">" }
illegal_chars = { x: 0 for x in bracket_map.values() }
for line in open("input.txt", "r"):
    stack = []
    for bracket in line.rstrip():
        if bracket in ("(", "[", "{", "<"):
            stack.append(bracket_map[bracket])
        elif stack.pop() != bracket:
            illegal_chars[bracket] += 1
            break
print(illegal_chars[")"]*3 + illegal_chars["]"]*57 + illegal_chars["}"]*1197 + illegal_chars[">"]*25137)
