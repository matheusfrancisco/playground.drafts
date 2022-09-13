from __future__ import print_function

"""
Time complexity O(n)
Space complexityO(1)

"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def calculate_lenght(p2):
    current = p2
    c = 0
    while True:
        current = current.next
        c += 1
        if current == p2:
            break
    return c


def start_node(head, lenght):
    p1 = head
    p2 = head
    while lenght > 0:
        p2 = p2.next
        lenght -= 1

    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1


def find_cycle_start(head):
    lenght = 0
    p1, p2 = head.next, head
    while p1.next is not None:
        p1 = p1.next.next
        p2 = p2.next
        if p1 == p2:
            lenght = calculate_lenght(p2)
            break
    return start_node(head, lenght)


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()
