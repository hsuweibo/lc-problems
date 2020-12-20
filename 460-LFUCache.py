import unittest


class LFUCache:
    """Constant time runtime with O(capacity) space"""

    def __init__(self, capacity: int):
        # A dictionary mapping each freq to a link list. Each link list is ordered from oldest to most recent
        self.recency = dict()
        self.nodes = dict()

        # A ptr to the list associated with the lowest frequency
        self.evict_list = None
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.nodes:
            key_node = self.nodes[key]
            self.increase_node_freq(key_node)
            return key_node.val
        return -1

    def put(self, key: int, val: int) -> None:
        if self.capacity == 0:
            return

        if key in self.nodes:
            key_node = self.nodes[key]
            key_node.val = val
        else:
            if self.size == self.capacity:
                self.evict()

            key_node = Node(key, val)
            self.nodes[key] = key_node
            self.size += 1

        self.increase_node_freq(key_node)

    def evict(self):
        # Remove the head of the evict list, and update next node's prev ptr. The prev of evicted_node should be None.
        evicted_node = self.evict_list.head
        if evicted_node.next:
            evicted_node.next.prev = None
        del self.nodes[evicted_node.key]

        # Update head
        self.evict_list.head = self.evict_list.head.next

        # If the evict list is now empty, the new evict list is the list with the next smallest frequency
        if self.evict_list.head is None:
            old_evict_list = self.evict_list
            self.evict_list = old_evict_list.next
            self.remove_list(old_evict_list)

        self.size -= 1

    def increase_node_freq(self, node):
        """
            Given a node, increase its frequency. More specifically, we move the node from the current list to the
            list associated with node.freq + 1. As we do so, we need to update the head/tail of the current list, create
            the list with the increase frequency if it doesn't exist, or update its tail if it exists, then update the
            evict list pointer
        """
        old_freq_list = None
        if node.freq in self.recency:
            old_freq_list = self.recency[node.freq]

            if old_freq_list.head is node:
                old_freq_list.head = node.next
            if old_freq_list.tail is node:
                old_freq_list.tail = node.prev

            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

        node.freq += 1
        node.next = None
        node.prev = None

        if node.freq in self.recency:
            new_freq_list = self.recency[node.freq]
            new_freq_list.tail.next = node
            node.prev = new_freq_list.tail
            new_freq_list.tail = node
        else:
            new_freq_list = DoublyLinkedList(node.freq, node, node)
            new_freq_list.prev = old_freq_list

            # If the old list exists (i.e., the node is not a fresh new node), and we get to this line, it must be
            # that old_freq_list.next.freq > node.freq. So we update the pointers so that the new list falls between
            # old_freq_list, and old_freq_list.next
            if old_freq_list:
                new_freq_list.next = old_freq_list.next
                if old_freq_list.next:
                    old_freq_list.next.prev = new_freq_list
                old_freq_list.next = new_freq_list

            self.recency[node.freq] = new_freq_list

        # If the old list existed and is now empty due to the movement of the node, remove the list.
        if old_freq_list and old_freq_list.head is None:
            # If the old list is the evict list, the new list is now the list with lowest freq
            if old_freq_list is self.evict_list:
                self.evict_list = new_freq_list
            self.remove_list(old_freq_list)

        # Set the evict list to the new list if there wasn't one before (i.e., the cache was empty),
        # or if the evict list existed but a new node (with freq 1) was inserted
        if self.evict_list is None or new_freq_list.freq < self.evict_list.freq:
            self.evict_list = new_freq_list

    def remove_list(self, lst):
        """
            Remove a list, and update its next/prev pointer.
            If the lst is the evict list, the evict list pointer should be updated in the calling function.
        """
        if lst.prev:
            lst.prev.next = lst.next
        if lst.next:
            lst.next.prev = lst.prev

        del self.recency[lst.freq]


class DoublyLinkedList():
    def __init__(self, freq, head=None, tail=None):
        # The head and the tail of the list. They are Node objects
        self.head = head
        self.tail = tail

        # Pointer to the previous list (the list with the next highest freq that is smaller than curr list's freq),
        # and the next list (the list with the next lowest freq that is higher than current list's freq)
        self.prev = None
        self.next = None

        # The frequency of all nodes contained in this list
        self.freq = freq


class Node():
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
        self.freq = 0


class TestLFU(unittest.TestCase):
    def test_input1(self):
        lfu = LFUCache(2)
        lfu.put(1, 1)
        lfu.put(2, 2)
        self.assertEqual(lfu.get(1), 1)
        lfu.put(3, 3)
        self.assertEqual(lfu.get(2), -1)
        self.assertEqual(lfu.get(3), 3)
        lfu.put(4, 4)
        self.assertEqual(lfu.get(1), -1)
        self.assertEqual(lfu.get(3), 3)
        self.assertEqual(lfu.get(4), 4)


    def test_input2(self):
        lfu = LFUCache(4)
        lfu.put(1, 1)
        lfu.put(2, 2)
        lfu.put(3, 3)
        lfu.put(4, 4)
        lfu.put(2, 2)
        lfu.put(5, 5)
        self.assertEqual(lfu.get(1), -1)
        self.assertEqual(lfu.get(3), 3)
        self.assertEqual(lfu.get(2), 2)
        lfu.put(6, 6)
        self.assertEqual(lfu.get(4), -1)
        self.assertEqual(lfu.get(2), 2)
        lfu.put(2, 123)
        self.assertEqual(lfu.get(2), 123)
        lfu.get(5)
        lfu.get(5)
        lfu.get(3)
        self.assertEqual(lfu.get(6), 6)
        lfu.put(7, 7)
        self.assertEqual(lfu.get(6), -1)


if __name__ == '__main__':
    unittest.main()
