from listNode import ListNode

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

def addTwoNumbers(l1, l2):
    cur1, cur2 = l1, l2
    cur = head = ListNode(0)
    flag = 0
    while cur1 or cur2 or flag:
        val1 = cur1.val if cur1 else 0
        val2 = cur2.val if cur2 else 0
        value = val1+val2+flag
        remain = value % 10
        cur.next = ListNode(remain)
        flag = 1 if value >= 10 else 0
        cur = cur.next
        if cur1: cur1 = cur1.next
        if cur2: cur2 = cur2.next
    return head.next

print(addTwoNumbers(l1,l2).print())