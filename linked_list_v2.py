#!/usr/bin/env python3


# insert
# remove

class LinkedList(object):
    def __init__(self):
        self.head = ListNode(None, marker="dummy head")
        self.tail = ListNode(None, marker="dummy tail")

        self.head.next = self.tail
        self.head.prev = self.tail

        self.tail.next = self.head
        self.tail.prev = self.head

        self.size = 0

    def insert_at_head(self, d):
        ln = ListNode(d)
        ln.next = self.head.next
        ln.next.prev = ln
        self.head.next = ln
        ln.prev = self.head
        self.size += 1


    def insert_at_tail(self, d):
        ln = ListNode(d)
        self.tail.prev.next=ln
        ln.next=self.tail
        self.tail.prev=ln
        ln.prev=self.tail.prev
        self.size += 1

    def delete_from_head(self,d):
        p=self.head.next
        while p.data != "dummy tail":
            if (p.data == d):
                p.prev.next=p.next
                p.next.prev=p.prev
                p=None
                self.size -= 1
                break
            p=p.next

    def delete_from_tail(self,d):
        p=self.tail.prev
        while p.marker != "dummy head":
            if(p.data==d):
                p.next.prev=p.prev
                p.prev.next=p.next
                p=None
                self.size -= 1
                break
            p=p.prev

    def print(self):
        p = self.head.next
        output = ""
        while p.marker != "dummy tail":
            output += str(p.data) + "->"
            p = p.next
        print(output)


    def get_size(self):
        return self.size

class ListNode(object):
    def __init__(self, data, p=None, n=None, marker=None):
        self.data = data
        self.prev = p
        self.next = n
        self.marker = marker
        # dummy head -> marker = "dummy head"
        # dummy tail -> marker = "dummy tail"

if __name__ == "__main__":
    l = LinkedList()

    for i in range(10):
        #l.insert_at_head(i)
        l.insert_at_head(i)
        l.print()
    l.print()

    for i in range(10):
        l.delete_from_tail(i)
        l.print()
    l.print()


    for i in range(10):
        #l.insert_at_head(i)
        l.insert_at_tail(i)
        l.print()
    l.print()

    for i in range(10):
        l.delete_from_head(i)
        l.print()
    l.print()
