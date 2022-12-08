from data import practice, full_data
import numpy as np

def find_num_trees_visible(line_of_trees):
    num_trees_visible = 0
    visible = []
    prev_highest_tree_height = -1
    for tree_height in line_of_trees:
        if tree_height > prev_highest_tree_height:
            visible.append(True)
            prev_highest_tree_height = tree_height
        else:
            visible.append(False)
    return np.array(visible, dtype=np.uint8)

def part_1(raw_dataset=practice):
    dataset = np.array([[int(tree) for tree in row] for row in raw_dataset.split("\n")], dtype=np.uint8)

    visible = np.zeros(dataset.shape)

    for idx in range(dataset.shape[0]):

        row = dataset[idx,:]
        rev_row = row[::-1]
        col = dataset[:,idx]
        rev_col = col[::-1]

        visible[idx,:] += find_num_trees_visible(row)
        visible[idx,:] += find_num_trees_visible(rev_row)[::-1]
        visible[:,idx] += find_num_trees_visible(col)
        visible[:,idx] += find_num_trees_visible(rev_col)[::-1]    

    return sum(sum(visible.astype(bool)))
        

    

if __name__ == "__main__":
    assert(part_1()==21)
    print(part_1(full_data))