class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass

if __name__ == "__main__":
    sol = Solution()

    testone_list1 = [1, 2, 4]
    testone_list2 = [1, 3, 4]
    print(f"Test case 1: {sol.mergeTwoLists(testone_list1, testone_list2)}")

    testtwo_list1 = []
    testtwo_list2 = []
    print(f"Test case 2: {sol.mergeTwoLists(testtwo_list1, testtwo_list2)}")

    testthree_list1 = []
    testthree_list2 = [0]
    print(f"Test case 3: {sol.mergeTwoLists(testthree_list1, testthree_list2)}")
