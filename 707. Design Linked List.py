class ListNode:

    def __init__(self,val,next=None):
        self.val = val
        self.next = next
class MyLinkedList:

    def __init__(self):

        self.head = None
        

    def get(self, index: int) -> int:

        i=0
        curr = self.head
        while curr:
            if i==index:
                return curr.val
            curr = curr.next
            i+=1
        return -1
            
        

    def addAtHead(self, val: int) -> None:

        node = ListNode(val,self.head)
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        
        if not self.head:  # If the list is empty
            self.head = ListNode(val)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)
        

    def addAtIndex(self, index: int, val: int) -> None:

        
        
        if index == 0:
            self.addAtHead(val)
        # elif index==length:
        #     current = self.head
        #     while current:
        #         if not current.next:
        #             node = ListNode(val)
        #             current.next = node
        
        else:
            i = 0
            cur = self.head
            while cur:
                if i==index-1:
                    node = ListNode(val,cur.next)
                    cur.next = node
                    return
                i+=1
                cur = cur.next
        

    def deleteAtIndex(self, index: int) -> None:
        
        
        if index==0:
            

            self.head = self.head.next

        # elif index==length-1:

        #     cur = self.head
        #     while cur:
        #         if not cur.next.next:
        #             cur.next = None
        #         cur = cur.next
        
        # elif index==1:
        #     self.head.next = self.head.next.next
        
        # else:
        #     i==1
        #     slow = self.head.next
        #     fast = self.head.next.next
            
        #     while slow and fast:
        #         if i==index-1:
        #             slow.next = fast.next
        #         else:
        #             slow=slow.next
        #             fast=fast.next
        #         i+=1

        # curr = self.head
        # i = 0
        # while curr and curr.next:
        #     if i == index - 1:
        #         curr.next = curr.next.next
        #         return
        #     curr = curr.next
        #     i += 1
        curr = self.head
        i = 0

        # Traverse to the node just before the one to delete
        while curr and curr.next:
            if i == index - 1:
                if curr.next.next:  # If there's a node after the next one
                    curr.next = curr.next.next
                else:  # If we're deleting the last node
                    curr.next = None
                return
            curr = curr.next
            i += 1


        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)




### chatgpt's answer
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        node = ListNode(val, self.head)
        self.head = node

    def addAtTail(self, val: int) -> None:
        if not self.head:  # If the list is empty
            self.head = ListNode(val)
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        curr = self.head
        i = 0
        while curr:
            if i == index - 1:
                node = ListNode(val, curr.next)
                curr.next = node
                return
            curr = curr.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:  # If the list is empty, nothing to delete
            return

        if index == 0:  # If the head needs to be deleted
            self.head = self.head.next
            return

        curr = self.head
        i = 0
        while curr and curr.next:
            if i == index - 1:
                curr.next = curr.next.next
                return
            curr = curr.next
            i += 1
