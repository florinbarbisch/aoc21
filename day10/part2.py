bracket_map = { "(": ")", "[": "]", "{": "}", "<": ">" }
score_map = { ")": 1, "]": 2, "}": 3, ">": 4 }
scores = []
for line in open("input.txt", "r"):
    stack = []
    for bracket in line.rstrip():
        if bracket in ("(", "[", "{", "<"):
            stack.append(bracket_map[bracket])
        elif stack.pop() != bracket:
            break
    else:
        score = 0
        for bracket in reversed(stack):
            score = score*5 + score_map[bracket]
        scores.append(score)
scores.sort()
print(scores[len(scores)//2])