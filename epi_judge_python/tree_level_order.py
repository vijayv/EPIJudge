from test_framework import generic_test
from collections import deque

def binary_tree_depth_order(tree):
    if not tree:
        return []
    output = []
    queue = [(tree, 0)]

    while queue:
        curr, depth = queue.pop()
        try:
            output[depth].appendleft(curr.data)
        except IndexError:
            output.append(deque([curr.data]))

        if curr.left:
            queue.append((curr.left, depth+1))
        if curr.right:
            queue.append((curr.right, depth+1))

    return [list(c) for c in output]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
