def matching_lines(path, prefix):
    prefix_length = len(prefix)
    with open(path, "r") as file:
        for line in file:
            if line[0:prefix_length] == prefix:
                yield line


def count_bit_after_prefix(path, prefix):
    prefix_length = len(prefix)
    zeros, ones = 0, 0
    for line in matching_lines(path, prefix):
        if line[prefix_length] == "0":
            zeros += 1
        else:
            ones += 1
    return zeros, ones


def find_rating(path, next_bit):
    prefix = ""
    while True:
        zeros, ones = count_bit_after_prefix(path, prefix)
        if zeros + ones == 1: # found the one
            break
        prefix += next_bit(zeros, ones)

    num, *_ = matching_lines(path, prefix) # all items of the generator must be consumed
    return int(num, base=2)


path = "input.txt"
oxygen_generator_rating = find_rating(path, lambda zeros, ones: "1" if ones >= zeros else "0")
CO2_scrubber_rating     = find_rating(path, lambda zeros, ones: "0" if ones >= zeros else "1")
print(oxygen_generator_rating * CO2_scrubber_rating)