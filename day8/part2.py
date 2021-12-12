with open("input.txt", "r") as file:
    total = 0
    len_to_num = {2:1, 4:4, 3:7, 7:8}
    for line in file:
        input, output = line.rstrip().split(" | ")
        nums_with_len_5, nums_with_len_6 = [[], []]
        num_to_segments = {}
        for segments in input.split(" "):
            segments = frozenset(list(segments))
            length = len(segments)
            if len(segments) in len_to_num.keys():
                num_to_segments[len_to_num[length]] = segments
            elif length == 5: nums_with_len_5.append(segments) # 5: 2, 3, 5
            elif length == 6: nums_with_len_6.append(segments) # 6: 0, 6, 9
        # solve the remaining numbers with set operations
        for x in nums_with_len_5: # numbers (2, 3, 5)
            if   len(num_to_segments[4].difference(x)) == 2: num_to_segments[2] = x
            elif len(num_to_segments[7].difference(x)) == 0: num_to_segments[3] = x
            else:                                            num_to_segments[5] = x
        for x in nums_with_len_6: # numbers (0, 6, 9)
            if   len(num_to_segments[7].difference(x)) == 1: num_to_segments[6] = x
            elif len(num_to_segments[4].difference(x)) == 0: num_to_segments[9] = x
            else:                                            num_to_segments[0] = x
        segment_to_num = { v: k for k,v in num_to_segments.items()} # reverse dict
        # evaluate on output vars
        output_nums = output.split(" ")
        for i in range(len(output_nums)):
            total += segment_to_num[frozenset(list(output_nums[i]))] * (10**(3-i))
    print(total)