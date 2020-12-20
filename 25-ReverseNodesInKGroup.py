# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        if k == 1:
            return head

        curr = head
        segment_head = None
        prev_segment_tail = None
        segment_tail = None
        cnt = 1

        while curr:
            if cnt == 1:
                segment_head = curr
                segment_tail = curr
                curr = curr.next
                cnt += 1
            elif cnt <= k:
                tmp = curr.next
                curr.next = segment_head
                segment_head = curr
                curr = tmp

                if cnt == k:
                    if prev_segment_tail:
                        prev_segment_tail.next = segment_head
                    else:
                        head = segment_head

                    prev_segment_tail = segment_tail
                    segment_head = None
                    segment_tail = None
                    cnt = 1
                else:
                    cnt += 1

        # If there were no leftover segment, then set the previous segment's tail's next node to None.
        # If prev_segment_tail is None, it must be the linked list was empty initially
        if segment_head is None:
            if prev_segment_tail:
                prev_segment_tail.next = None
            else:
                head = None
        else:
            # In this case, there was a leftover segment with size less than k.
            # Reverse the leftover segment, and set the previous segment tail's next node accordingly
            segment_tail.next = None
            prev = None
            curr = segment_head
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            if prev_segment_tail:
                prev_segment_tail.next = segment_tail
            else:
                head = segment_tail

        return head