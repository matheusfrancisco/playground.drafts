def remove_duplicates(linked_list):
    """
      Remove duplicate values from linked list
      Time Best Case: O(n)
    """
    if len(linked_list) == 0:
        return linked_list

    node = linked_list._head
    if node:
        values = {node.value: True}
        while node.next:
            if node.next.value in values:
                node.next = node.next.next
            else:
                values[node.next.value] = True
                node = node.next
    return linked_list
