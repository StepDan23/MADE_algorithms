import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinTree:
    def __init__(self):
        self.root = None

    def _insert(self, node, val):
        if node is None:
            return Node(val)
        if val > node.val:
            node.right = self._insert(node.right, val)
        elif val < node.val:
            node.left = self._insert(node.left, val)
        return node

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None
        elif val > node.val:
            node.right = self._delete(node.right, val)
        elif val < node.val:
            node.left = self._delete(node.left, val)
        elif node.left is None:
            node = node.right
        elif node.right is None:
            node = node.left
        else:
            node.val = find_max_in_tree(node.left)
            node.left = self._delete(node.left, node.val)
        return node

    def delete(self, val):
        self.root = self._delete(self.root, val)

    def _exists(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        elif val > node.val:
            return self._exists(node.right, val)
        else:
            return self._exists(node.left, val)

    def exists(self, val):
        return self._exists(self.root, val)

    def prev(self, val):
        node = self.root
        res = None
        while node is not None:
            if val > node.val:
                res = node.val
                node = node.right
            else:
                node = node.left
        return res

    def next(self, val):
        node = self.root
        res = None
        while node is not None:
            if val < node.val:
                res = node.val
                node = node.left
            else:
                node = node.right
        return res


def find_max_in_tree(tree_node):
    if tree_node is None:
        return None
    while tree_node.right:
        tree_node = tree_node.right
    return tree_node.val


tree = BinTree()
for line in sys.stdin.read().splitlines():
    command, value = line.split()
    value = int(value)
    if command == 'insert':
        tree.insert(value)
    elif command == 'delete':
        tree.delete(value)
    elif command == 'exists':
        print(str(tree.exists(value)).lower())
    elif command == 'next':
        print(str(tree.next(value)).lower())
    elif command == 'prev':
        print(str(tree.prev(value)).lower())
    else:
        raise ValueError('Unknown command')
