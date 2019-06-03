import hashlib


class DataNode:

    _data = None
    _prev_hash = None
    _modified_node = None
    _next_node = None

    def __init__(self, data, next_node=None):
        self._data = data
        if next_node is not None:
            if isinstance(next_node, DataNode):
                self._next_node = next_node
            else:
                print('Please provide the nex_node that is an instance of DataNode')

    def get_previous_hash(self):
        return self._prev_hash

    def set_previous_hash(self, prev_hash):
        self._prev_hash = prev_hash

    def get_modified_node(self):
        return self._modified_node

    def set_modified_node(self, node):
        self._modified_node = node

    def to_string(self):
        return '{}\n{}'.format(self._data, self._prev_hash)

    def to_hash(self):
        final_string = self.to_string()
        return hashlib.sha256(final_string.encode('utf-8')).hexdigest()

    def __str__(self):
        return 'Data: {}\nPrevious_Hash: {}'.format(self._data, self._prev_hash)

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, node):
        if isinstance(node, DataNode):
            self._next_node = node
        else:
            print('Please provide an object that is an instance of DataNode')


class SecureLinkedList:
    def __init__(self):
        self._head_node = DataNode(data='Genesis')
        self._count = 0

    def get_head_node(self):
        return self._head_node

    def get_count(self):
        return self._count

    def insert(self, node):
        temp_node = self._head_node
        node.set_previous_hash(temp_node.to_hash())
        if isinstance(node, DataNode):
            node.next_node = temp_node
            self._head_node = node
            self._count += 1
        else:
            print('Argument must be an instance of DataNode')

    def find_node(self, previous_hash):
        # you find a node using its previous_hash, this is also helpful to know
        # what was the state of the linked list before this node
        temp_node = self.get_head_node()
        while temp_node.get_previous_hash() != previous_hash:
            temp_node = temp_node.next_node
            if temp_node.get_modified_node() is not None:
                temp_node2 = temp_node.get_modified_node()

                while temp_node2 is not None:
                    if temp_node2.get_previous_hash() == previous_hash:
                        return temp_node2
                    temp_node2 = temp_node2.get_modified_node()

        return temp_node

    def modify_node(self, previous_hash, new_node):
        that_node = self.find_node(previous_hash)
        new_node.set_previous_hash(that_node.to_hash())
        that_node.set_modified_node(node=new_node)
        return that_node.get_modified_node().get_previous_hash()
