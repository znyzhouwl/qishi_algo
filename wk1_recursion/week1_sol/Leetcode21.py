# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    if l1.val > l2.val:
        l1, l2 = l2, l1
        head = l1
    else:
        head = l1

    while l1.next is not None:
        if l1.next.val > l2.val:
            l1.next, l2 = l2, l1.next
            l1 = l1.next
        else:
            l1 = l1.next
    l1.next = l2
    return head
