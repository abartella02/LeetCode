class Node:
    def __init__(self, key: int, value: int):
        self.next = None
        self.prev = None
        self.key = key
        self.value = value


class LRUCache:

    def __init__(self, capacity: int):
        self.__head = None
        self.__tail = None
        self.__capacity = capacity
        self.__len = 0
        self.__hash = {}

    def __moveToFront(self, node: Node):
        if node is self.__head:
            return
        if node is self.__tail:
            self.__tail = node.prev

        old_head = self.__head
        self.__head = node
        self.__head.next = old_head
        self.__head.prev = None
        old_head.prev = self.__head
        if old_head.next == node:
            old_head.next = None

    def __removeLastNode(self):
        old_tail = self.__tail
        if self.__capacity == 1:
            self.__tail = self.__head
        else:
            self.__tail = old_tail.prev
            self.__tail.next = None

            del self.__hash[old_tail.key]
        del old_tail

    def get(self, key: int) -> int:
        node = self.__hash.get(key)
        if node is None:
            return -1
        self.__moveToFront(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        _hash = self.__hash
        if self.__head is None:
            new_node = Node(key=key, value=value)
            self.__head = new_node
            self.__tail = new_node
            _hash[key] = new_node
            self.__len += 1
            return

        node = _hash.get(key)
        if node:  # if node already exists
            node.value = value  # update value
        else:
            # create new node if doesn't exist
            node = Node(key=key, value=value)
            _hash[key] = node  # hash new node's value

        self.__moveToFront(node)  # move modified/new node to front

        if self.__len >= self.__capacity:
            # remove last node if capacity will be exceeded
            self.__removeLastNode()
        else:
            self.__len += 1


obj = LRUCache(capacity=2)
obj.put(2, 1)
obj.put(1, 1)
obj.put(2, 3)
obj.put(4, 1)
obj.get(1)
obj.get(2)
