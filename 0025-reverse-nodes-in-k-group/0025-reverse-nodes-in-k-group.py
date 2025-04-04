
class Solution(object):
    
    def reverseKGroup(self, head, k):
        l, node = 0, head
        while node:
            l += 1
            node = node.next
        if k <= 1 or l < k:
            return head
        node, cur = None, head
        for _ in xrange(k):
            nxt = cur.next
            cur.next = node
            node = cur
            cur = nxt
        head.next = self.reverseKGroup(cur, k)
        return node

    def reverseKGroup(self, head, k):
        if not head or not head.next or k <= 1:
            return head
        cur, l = head, 0
        while cur:
            l += 1
            cur = cur.next
        if k > l:
            return head
        dummy = pre = ListNode(0)
        dummy.next = head

        for i in xrange(l//k):
            
            node = None
            for j in xrange(k-1):
                nxt = head.next
                head.next = node
                node = head
                head = nxt
            
            tmp = head.next
            head.next = node
            pre.next.next = tmp
            tmp1 = pre.next
            pre.next = head
            head = tmp
            pre = tmp1
        return dummy.next
            