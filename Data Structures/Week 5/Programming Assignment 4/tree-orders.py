# python3

import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def print_tree(self):
        print(self.key)
        print(self.left)
        print(self.right)

    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.inorder_rec(0, self.result)
        return self.result

    def inorder_rec(self, i, res):
        if self.right[i] == -1 and self.left[i] == -1:
            # this is required because in original implementation
            # tree was checked till the leaf node next child but here
            # it is checked for only till leaf node
            res.append(self.key[i])
            return
        if self.left[i] != -1:
            self.inorder_rec(self.left[i], res)
        res.append(self.key[i])
        if self.right[i] != -1:
            self.inorder_rec(self.right[i], res)

    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.preorder_rec(0, self.result)
        return self.result

    def preorder_rec(self, i, res):
        if self.left[i] == -1 and self.right[i] == -1:
            res.append(self.key[i])
            return
        res.append(self.key[i])
        if self.left[i] != -1:
            self.preorder_rec(self.left[i], res)
        if self.right[i] != -1:
            self.preorder_rec(self.right[i], res)

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.postorder_rec(0, self.result)
        return self.result

    def postorder_rec(self, i, res):
        if self.left[i] == -1 and self.right[i] == -1:
            res.append(self.key[i])
            return
        if self.left[i] != -1:
            self.postorder_rec(self.left[i], res)
        if self.right[i] != -1:
            self.postorder_rec(self.right[i], res)
        res.append(self.key[i])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
