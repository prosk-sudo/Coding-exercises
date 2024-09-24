class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

if __name__ == "__main__":
    sol = Solution()

    testone_list1 = list_to_linkedlist([1, 2, 4])
    testone_list2 = list_to_linkedlist([1, 3, 4])
    merged_list1 = sol.mergeTwoLists(testone_list1, testone_list2)
    print(f"Test case 1: {linkedlist_to_list(merged_list1)}")

    testtwo_list1 = list_to_linkedlist([])
    testtwo_list2 = list_to_linkedlist([])
    merged_list2 = sol.mergeTwoLists(testtwo_list1, testtwo_list2)
    print(f"Test case 2: {linkedlist_to_list(merged_list2)}")

    testthree_list1 = list_to_linkedlist([])
    testthree_list2 = list_to_linkedlist([0])
    merged_list3 = sol.mergeTwoLists(testthree_list1, testthree_list2)
    print(f"Test case 3: {linkedlist_to_list(merged_list3)}")
