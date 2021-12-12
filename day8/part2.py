def num_chars_not_in(A, B):
    return len(list(filter(lambda x: x not in list(B), list(A))))

def matches(A, B):
    if len(A) != len(B): return False
    return num_chars_not_in(A, B) == 0

with open("input.txt", "r") as file:
    total = 0
    len_to_num = {2:1, 4:4, 3:7, 7:8}
    for line in file:
        input, output = line.rstrip().split(" | ")
        nums_with_len_5, nums_with_len_6 = [[], []]
        num_mapping = {}
        for num in input.split(" "):
            length = len(num)
            if length in len_to_num.keys(): num_mapping[len_to_num[length]] = num
            elif length == 5: nums_with_len_5.append(num) # 5: 2, 3, 5
            elif length == 6: nums_with_len_6.append(num) # 6: 0, 6, 9
        for x in nums_with_len_5: # numbers (2, 3, 5)
            if   num_chars_not_in(num_mapping[4], x) == 2: num_mapping[2] = x
            elif num_chars_not_in(num_mapping[7], x) == 0: num_mapping[3] = x
            else:                                          num_mapping[5] = x
        for x in nums_with_len_6: # numbers (0, 6, 9)
            if   num_chars_not_in(num_mapping[7], x) == 1: num_mapping[6] = x
            elif num_chars_not_in(num_mapping[4], x) == 0: num_mapping[9] = x
            else:                                          num_mapping[0] = x
        # evaluate on output vars
        output_nums = output.split(" ")
        for i in range(len(output_nums)):
            for num, set in num_mapping.items():
                if matches(output_nums[i], set):
                    total += num * (10**(3-i))
                    break
    print(total)