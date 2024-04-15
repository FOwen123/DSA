from Linked_List_DS import LinkedList

def merge_sort(linked_list):
    # Sorts a linked list in ascending order
    # - Recursively divide the linked list into sublists containing a single node
    # - Repeatedly merge the sublists to produce sorted sublists until one remains
    
    # Returns a sorted linked list
    
    # Runs in O(kn log n) 
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    # Divide the unsorted list at midpoint into sublists
    # Takes O(k log n) time

    if linked_list == None or linked_list.head == None: 
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else: 
        size = linked_list.size()
        middle = size // 2
        mid_node = linked_list.node_at_index(middle - 1)

        left_half = linked_list 
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
    
        return left_half, right_half
    
def merge(left, right):
    # Merges two linked lists, sorting by data in nodes
    # Returns a new, merged list
    # Runs in O(n) time

    # Create a new linked list that contains nodes from merging left and right
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.add(0)

    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes for left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterative over left and right until we reach the tail node of either
    while left_head and right_head:
        left_data = left_head.data
        right_data = right_head.data
        if left_data < right_data:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            current.next_node = right_head
            right_head = right_head.next_node
        current = current.next_node

    # Append the remaining nodes, if any, from left and right to the merged list
    if left_head or right_head:
        current.next_node = left_head if left_head else right_head

    head = merged.head.next_node
    merged.head = head

    return merged

l = LinkedList()
l.add(10)
l.add(100)
l.add(1)
l.add(45)
l.add(15)
l.add(-1)
l.add(10000)

print(l)
sorted_linked_list = merge_sort(l)
print(sorted_linked_list)