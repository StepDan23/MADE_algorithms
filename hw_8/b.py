import sys


class Node:
    def __init__(self, val):
        self.val = val
        self.h = 0
        self.balance = 0
        self.left = None
        self.right = None

    def _get_left_h(self):
        if self.left is None:
            return 0
        return self.left.h

    def _get_right_h(self):
        if self.right is None:
            return 0
        return self.right.h

    def fix(self):
        self.h = max(self._get_left_h(), self._get_right_h()) + 1
        self.balance = self._get_left_h() - self._get_right_h()


class AvlTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def _small_rotate(node, direction):
        if direction == 'right':
            q = node.left
            node.left = q.right
            q.right = node
        elif direction == 'left':
            q = node.right
            node.right = q.left
            q.left = node
        node.fix()
        q.fix()
        return q

    def _big_rotate(self, node,  direction):
        if direction == 'right':
            node.left = self._small_rotate(node.left, direction='left')
            node = self._small_rotate(node, direction='right')
        elif direction == 'left':
            node.right = self._small_rotate(node.right, direction='right')
            node = self._small_rotate(node, direction='left')
        return node

    def _balance(self, node):
        node.fix()
        if node.balance == 2:
            if node.left.balance >= 0:
                return self._small_rotate(node, direction='right')
            return self._big_rotate(node, direction='right')
        if node.balance == -2:
            if node.right.balance <= 0:
                return self._small_rotate(node, direction='left')
            return self._big_rotate(node, direction='left')
        return node

    def _insert(self, node, val):
        if node is None:
            return Node(val)
        if val > node.val:
            node.right = self._insert(node.right, val)
        elif val < node.val:
            node.left = self._insert(node.left, val)
        return self._balance(node)

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None
        elif val > node.val:
            node.right = self._delete(node.right, val)
        elif val < node.val:
            node.left = self._delete(node.left, val)
        elif node.left is None and node.right is None:
            return None
        elif node.left is None:
            node = node.right
        elif node.right is None:
            node = node.left
        else:
            node.val = find_max_in_tree(node.left)
            node.left = self._delete(node.left, node.val)
        return self._balance(node)

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

    def _prev(self, node, val):
        if node is None:
            return None
        if val > node.val:
            k = self._prev(node.right, val)
            if k is None:
                return node.val
            return k
        else:
            return self._prev(node.left, val)

    def prev(self, val):
        return self._prev(self.root, val)

    def _next(self, node, val):
        if node is None:
            return None
        if val < node.val:
            k = self._next(node.left, val)
            if k is None:
                return node.val
            return k
        else:
            return self._next(node.right, val)

    def next(self, val):
        return self._next(self.root, val)


def find_max_in_tree(tree_node):
    if tree_node is None:
        return None
    while tree_node.right:
        tree_node = tree_node.right
    return tree_node.val


tree = AvlTree()
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
