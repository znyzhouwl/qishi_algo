# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head: ListNode, val: int) -> ListNode:
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if head is None:
        return head
    p = head

    while p.next is not None:
        if p.next.val == val:
            if p.next.next is None:
                p.next = None

            else:
                p.next = p.next.next

        else:
            p = p.next
    if head.val == val:
        return head.next
    return head
