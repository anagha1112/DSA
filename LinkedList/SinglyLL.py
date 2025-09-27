from Node import Node   # import Node class from Node.py

class SinglyLL:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def traversal(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr = curr.next
        print()


    def insert_at(self, val, pos):

        new_node = Node(val)

        if pos == 0:

            new_node.next = self.head
            self.head = new_node

        else:

            curr = self.head
            count = 0

            while curr is not None and count < pos - 1:

                curr = curr.next
                count += 1

            if curr is None:
                print("Position out of range")
                return

            new_node.next = curr.next
            curr.next = new_node

    def delete(self, val):

        temp = self.head

        if temp is not None:

            if temp.val == self.head.val:

                self.head = self.head.next

            else:

                found = false
                prev = None

                while temp is not None:

                    if temp.val == val:

                        found = True
                        break

                    prev = temp
                    temp = temp.next

                if found:
                    prev.next = temp.next
                    return

                else:

                    print("Node not found")
