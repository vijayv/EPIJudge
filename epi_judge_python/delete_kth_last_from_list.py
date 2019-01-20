from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    prev = None
    curr, runner = L, L

    for _ in range(k):
        if runner:
            runner = runner.next
        else:
            raise ValueError('invalid input provided to function')

    while runner:
        prev, curr, runner = curr, curr.next, runner.next

    if prev:
        prev.next = curr.next
    else:
        L = curr.next

    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
