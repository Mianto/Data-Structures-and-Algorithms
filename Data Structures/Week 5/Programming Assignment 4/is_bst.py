#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def IsBinarySearchTree(tree, nodes):
    # Implement correct algorithm here
    if nodes == 0:
        return True
    result = list()
    inorder_rec(tree, 0, result)
    if sorted(result) != result:
        return False
    return True


def inorder_rec(tree, i, res):
    if tree[i][1] == -1 and tree[i][2] == -1:
        res.append(tree[i][0])
        return
    if tree[i][1] != -1:
        inorder_rec(tree, tree[i][1], res)
    res.append(tree[i][0])
    if tree[i][2] != -1:
        inorder_rec(tree, tree[i][2], res)


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))

    if IsBinarySearchTree(tree, nodes):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
