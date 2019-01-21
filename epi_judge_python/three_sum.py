from test_framework import generic_test


# There is a more optimal solution than this that allows for O(n) rather than
# O(n^2). However, it requires non-trivial intuition. We can also probably
# improve this solution to use no space by using binary search instead of a set.

def has_three_sum(A, t):
    A.sort()
    vals = set(A)

    for c1 in A:
        for c2 in A:
            temp = t - (c1 + c2)
            if temp in vals:
                return True

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("three_sum.py", "three_sum.tsv",
                                       has_three_sum))
