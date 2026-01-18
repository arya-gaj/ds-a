class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            node = prev
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next

            cur = prev.next
            nxt = cur.next

            for _ in range(k - 1):
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = cur.next

            prev = cur