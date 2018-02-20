
class Node(object):

    def __init__(self, val, next=None, prev=None):
        self.val = val 
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.val) + ' '

class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, n):
        n.next = self.head
        if self.head:
            self.head.prev = n
        self.head = n 
        n.prev = None

    def delete(self, n):
        if n.prev:
            n.prev.next = n.next
        else:
            self.head = n.next 

        if n.next:
            n.next.prev = n.prev 

    def search(self, val):
        x = self.head 
        while x and x.val != val:
            x = x.next 
        return x

    def even_before_odd(self):
        even_head = self.head 
        cur = self.head 
        while cur:
            next = cur.next 
            if cur.val % 2 == 0 and cur != even_head:
                # remove cur node 
                if cur.prev:
                    cur.prev.next = cur.next 
                
                if cur.next:
                    cur.next.prev = cur.prev 

                # put in front of last even 
                if even_head.val % 2 == 0:
                    cur.next = even_head.next 
                    even_head.next = cur 
                    if cur.next:
                        cur.next.prev = cur
                    even_head = cur
                else:
                    cur.next = even_head
                    even_head = cur
                    self.head = even_head

            cur = next

    def __repr__(self):
        s = 'linked list: '
        nxt = self.head 
        while nxt:
            s += str(nxt)
            nxt = nxt.next
        return s

if __name__ == '__main__':

    # ll = LinkedList()
    # for i in reversed(range(10)):
    #     ll.insert(Node(i))
    # print(ll)
    # five = ll.search(5)
    # print(five)
    # ll.delete(five)
    # print(ll)

    # ll.even_before_odd()
    # print(ll)

    ll = LinkedList()
    for i in reversed([8, 12, 10, 5]):
        ll.insert(Node(i))
    print(ll)
    ll.even_before_odd()
    print(ll)





