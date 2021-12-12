bracket_map = { "(": ")", "[": "]", "{": "}", "<": ">" }
score_map = { ")": 1, "]": 2, "}": 3, ">": 4 }
scores = []
for line in open("input.txt", "r"):
    stack = []
    corrupt = False
    for bracket in list(line.rstrip()):
        if bracket in ("(", "[", "{", "<"):
            stack.append(bracket_map[bracket])
        elif stack[-1] == bracket:
            stack.pop()
        else:
            corrupt = True
            break
    if not corrupt and len(stack) > 0:
        score = 0
        stack.reverse()
        for bracket in stack:
            score = score*5 + score_map[bracket]
        scores.append(score)
scores.sort()
print(scores[len(scores)//2])