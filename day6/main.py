from data import example, practice_1, practice_2, practice_3, practice_4, full_data

def contains_duplicates(buffer, buffer_size):
    return len(set(buffer)) == buffer_size

def find_unique_char_sequence(data, buffer_size):
    buffer = list(data[:buffer_size])
    marker=buffer_size
    for idx, char in enumerate(data[buffer_size:]):
        if contains_duplicates(buffer, buffer_size):
            break
        buffer_idx = idx%buffer_size
        buffer[buffer_idx] = char
        marker += 1
    return marker

def part_1(data=example):
    return find_unique_char_sequence(data, 4)

def part_2(data=example):
    return find_unique_char_sequence(data, 14)


if __name__ == "__main__":
    print(part_1())
    print(part_1(practice_1))
    print(part_1(practice_2))
    print(part_1(practice_3))
    print(part_1(practice_4))
    print(part_1(full_data))
    print("=============")
    print(part_2())
    print(part_2(practice_1))
    print(part_2(practice_2))
    print(part_2(practice_3))
    print(part_2(practice_4))
    print(part_2(full_data))