from linkedlists import LinkedList


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.insert_after_node("A", "E")

llist.print_list()