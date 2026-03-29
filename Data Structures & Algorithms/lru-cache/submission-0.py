class Node:
    __slots__ = 'prev', 'next', 'key', 'value'

    def __init__(self, key = 0, value = 0):
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity: int):
        self.dummy = Node()
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy
        self.capacity = capacity
        self.key_to_value = {}

    def get_node(self, key):
        if not key in self.key_to_value:
            return None
        node = self.key_to_value[key]
        self.delete_node(node)
        self.push_to_top(node)
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.value = value
            return
        self.key_to_value[key] = node = Node(key, value)
        self.push_to_top(node)
        if len(self.key_to_value) > self.capacity:
            last_node = self.dummy.prev
            self.delete_node(last_node)
            del self.key_to_value[last_node.key]

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def push_to_top(self, node) -> None:
        node.next = self.dummy.next
        self.dummy.next.prev = node
        node.prev = self.dummy
        self.dummy.next = node


        
