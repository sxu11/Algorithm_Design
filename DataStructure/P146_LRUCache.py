class Node():
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = {}  # key: Node
        self.capacity = capacity
        self.size = 0
        # self.timer = 0
        self.head = Node()  # least recent used
        self.tail = Node()  # most recent used
        self.head.next, self.tail.prev = self.tail, self.head

    def get_list_size(self):
        node = self.head
        size = 1
        while node.next:
            node = node.next
            size += 1
        return size

    def get_list(self):
        node = self.head
        alist = [None]
        while node.next:
            node = node.next
            alist.append(node.val)
        return alist

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # self.timer += 1
        if key in self.dict:
            # self.dict[key] = (self.dict[key][0], self.timer)

            # TODO: Move self.dict[key] near the tail
            self.dict[key].prev.next, self.dict[key].next.prev = self.dict[key].next, self.dict[key].prev
            # self._remove(self.dict[key])

            self.tail.prev.next, self.dict[key].prev, self.tail.prev, self.dict[key].next = self.dict[
                                                                                                key], self.tail.prev, \
                                                                                            self.dict[key], self.tail
            # self._add(self.dict[key])

            res = self.dict[key].val
        else:
            res = -1

        # print "after get %d, list:"%(key), self.get_list()
        # print "self.tail.prev.val:", self.tail.prev.val

        return res

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # if key in self.dict:
        #     self._remove(self.dict[key])
        # n = Node(key, value)
        # self._add(n)
        # self.dict[key] = n
        # if len(self.dict) > self.capacity:
        #     n = self.head.next
        #     self._remove(n)
        #     del self.dict[n.key]

        # self.timer += 1
        if key in self.dict:
            # self.dict[key][0] = value
            # self.dict[key][1] = self.timer
            # self.dict[key] = (value, self.timer)
            self.dict[key].val = value
            # TODO: Move self.dict[key] near the tail

            self.dict[key].prev.next, self.dict[key].next.prev = self.dict[key].next, self.dict[key].prev
            # self._remove(self.dict[key])

            self.tail.prev.next, self.dict[key].prev, self.tail.prev, self.dict[key].next = self.dict[
                                                                                                key], self.tail.prev, \
                                                                                            self.dict[key], self.tail
            # self._add(self.dict[key])


        else:

            # self.dict[key] = (value, self.timer)
            # TODO: set and add self.dict[key] near the tail
            new_node = Node(key, value)
            self.dict[key] = new_node
            # self._add(new_node)

            # self.tail.prev.next, new_node.prev = new_node, self.tail.prev
            # self.tail.prev, new_node.next = new_node, self.tail

            self.tail.prev.next, self.dict[key].prev, self.tail.prev, self.dict[key].next = self.dict[
                                                                                                key], self.tail.prev, \
                                                                                            self.dict[key], self.tail

            self.size += 1

            if self.size > self.capacity:
                # evict the oldest one w/ O(1)
                # min_time_stamp = self.timer
                # LRU_key = key
                # for one_key in self.dict:
                #     '''
                #     A little awkward here
                #     Is this O(1)?!
                #     '''
                #     if self.dict[one_key][1] < min_time_stamp:
                #         min_time_stamp = self.dict[one_key][1]
                #         LRU_key = one_key

                # self.dict.pop(self.head.next.key) # TODO: the order of this two!!! 3 hours wasted!!!
                del self.dict[self.head.next.key]
                # self._remove(self.head.next) # TODO: the order of this two!!! 3 hours wasted!!!
                # self.head.next, self.head.next.next.prev = self.head.next.next, self.head

                # n = self.head.next.next
                # self.head.next, n.prev = self.head.next.next, self.head.next.prev
                self.head.next.next.prev, self.head.next = self.head.next.prev, self.head.next.next
                # TODO: This is the trickest error I have ever made!!!
                # Even though RHS is fine, the LFS order was not fine!!!!

                self.size -= 1

        return

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)