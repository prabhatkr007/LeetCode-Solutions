"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        if head is None:
            return 
        d={}
        cur=head
        while cur!=None:
            d[cur]=Node(cur.val)
            cur=cur.next
        cur=head
        while cur:
            if cur.next:
                d[cur].next=d[cur.next]
            if cur.random:
                d[cur].random=d[cur.random]
            cur=cur.next
        return d[head]
