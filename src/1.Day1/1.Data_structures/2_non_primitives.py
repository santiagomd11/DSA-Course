# Array
a = [1, 2, 3, 4, 5]
print(f'array: {a}')

# Stack
stack = [1, 2,]
print(f'stack: {stack}')
stack.append(3)
print(f'stack after push: {stack}')
stack.pop()
print(f'stack after pop: {stack}')

# Queue
queue = [1, 2, 3, 4, 5]
print(f'queue: {queue}')
queue.append(6)
print(f'queue after push: {queue}')
queue.pop(0)
print(f'queue after pop: {queue}')

# Hash Table
hash_table = {'a': 1, 'b': 2, 'c': 3}
print(f'hash table: {hash_table}')
print(f'hash table value for key b: {hash_table["b"]}')
hash_table['d'] = 4
print(f'hash table after adding key d: {hash_table}')

# Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
def print_linked_list(head: Node):
    while head:
        print(head.data, end=' -> ')
        head = head.next
    print('None')

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
print_linked_list(head)

# Tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
