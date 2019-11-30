class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def print(self):
        List = []
        while 1:
            List.append(self.val)
            if not self.next:
                break
            else:
                self = self.next
        return List