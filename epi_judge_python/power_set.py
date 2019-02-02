from test_framework import generic_test, test_utils


def generate_power_set(S):

    output = [[]]

    def helper(S, so_far=[], output=[]):
        if not len(S):
            output.append(so_far)
        else:
            helper(S[1:], so_far + [S[0]], output)
            helper(S[1:], so_far, output)

    for idx, num in enumerate(S):
        helper(S[idx+1:], [num], output)

    return output


if __name__ == '__main__':
    print(generate_power_set([0]))
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
