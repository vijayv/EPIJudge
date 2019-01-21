from test_framework import generic_test


# We only have to reverse the second half of the list because we only need to
# check half to see if it matches with the other half.
def is_linked_list_a_palindrome(L):

    def reverse(head):
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp

        return prev

    if not L:
        return True

    slow = L
    runner = L
    while runner and runner.next:
        slow = slow.next
        runner = runner.next.next

    Lr = reverse(slow)

    curr = L
    curr_r = Lr
    while curr_r:
        if curr.data != curr_r.data:
            return False
        curr, curr_r = curr.next, curr_r.next

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
