from data import example, practice_1, practice_2, practice_3, practice_4, full_data

def contains_duplicates(buffer, buffer_size):
    return len(set(buffer)) == buffer_size

def contains_duplicates_slower(buffer, buffer_size):
    match_found = False
    for idx in range(buffer_size**2):
        idx_1, idx_2 = idx//buffer_size, idx%buffer_size
        if idx_1 >= idx_2:
            continue
        if buffer[idx_1] == buffer[idx_2]:
            match_found=True
            break
    
    return match_found

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
    # print(part_1())
    # print(part_1(practice_1))
    # print(part_1(practice_2))
    # print(part_1(practice_3))
    # print(part_1(practice_4))
    # print(part_1(full_data))
    # print("=============")
    # print(part_2())
    # print(part_2(practice_1))
    # print(part_2(practice_2))
    # print(part_2(practice_3))
    # print(part_2(practice_4))
    # print(part_2(full_data))

    import timeit

    func_1_true = lambda: contains_duplicates([0,1,2,0],4)
    func_1_false = lambda: contains_duplicates([0,1,2,3],4)

    func_2_true = lambda: contains_duplicates_slower([0,0,2,2],4)
    func_2_false = lambda: contains_duplicates_slower([0,1,2,3],4)

    print(timeit.timeit(func_1_true))    
    print(timeit.timeit(func_1_false))    
    print(timeit.timeit(func_2_true))    
    print(timeit.timeit(func_2_false))    

    # print(timeit.timeit(lambda:part_1(full_data), number=10000))
    # print(timeit.timeit(lambda:part_2(full_data), number=10000))