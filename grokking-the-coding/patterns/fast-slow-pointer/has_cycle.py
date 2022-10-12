class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    """Time complexity: O(n), Space Complexity: O(1)"""
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True  # found the cycle
    return False


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))


"""
Problem 1: Given the head of a LinkedList with a cycle, find the length of the cycle.
Solution: 
    Solution: We can use the above solution to find the cycle in the
    LinkedList. Once the fast and slow pointers meet, we can save the 
    slow pointer and iterate the whole cycle with another pointer 
    until we see the slow pointer again to find the length of the cycle.

"""


def lenght_of_list():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next

    fast = head.next
    slow = head

    found = True
    while found:
        if fast == slow:
            found = False
            break
        fast = fast.next.next
        slow = slow.next

    count = 0
    while True:
        fast = fast.next
        count += 1

        if fast == slow:
            break
    return count


def find_cycle_length(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:  # found the cycle
            return calculate_cycle_length(slow)

    return 0


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length
