def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    aux = ListNode(0)
    current_head = aux
    while (l1 != None or l2 != None or carry != 0):
        val_list_1 = l1.val if l1 else 0
        val_list_2 = l2.val if l2 else 0
        sum_list = val_list_1 + val_list_2 + carry
        carry = sum_list // 10 
        new_node = ListNode(sum_list % 10)
        current_head.next = new_node
        current_head = new_node
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    return aux.next
        
