from test_framework import generic_test, test_utils

def phone_mnemonic(phone_number):

    mapping = {
        '0': ['0'],
        '1': ['1'],
        '2': ['A', 'B', 'C'],
        '3': ['D', 'E', 'F'],
        '4': ['G', 'H', 'I'],
        '5': ['J', 'K', 'L'],
        '6': ['M', 'N', 'O'],
        '7': ['P', 'Q', 'R', 'S'],
        '8': ['T', 'U', 'V'],
        '9': ['W', 'X', 'Y', 'Z'],
    }

    def helper(digits, so_far="", output=[]):
        if len(digits) == 0:
            output.append(so_far)
            return
        remaining = "" if len(digits) == 1 else digits[1:]
        for c in mapping.get(digits[0]):
            helper(remaining, so_far + c, output)


    output = []
    helper(phone_number, "", output)
    return output


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
