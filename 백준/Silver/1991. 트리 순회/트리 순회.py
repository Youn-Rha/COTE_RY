import sys

def input():
    return sys.stdin.readline().strip()

class Node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left if left != '.' else None
        self.right = right if right != '.' else None

    def preorder(self):
        print(self.item, end="")
        if self.left is not None:
            tree[self.left].preorder()
        if self.right is not None:
            tree[self.right].preorder()

    def inorder(self):
        if self.left is not None:
            tree[self.left].inorder()
        print(self.item, end="")
        if self.right is not None:
            tree[self.right].inorder()

    def postorder(self):
        if self.left is not None:
            tree[self.left].postorder()
        if self.right is not None:
            tree[self.right].postorder()
        print(self.item, end="")

# main
if __name__ == "__main__":
    N = int(input())
    tree = {}

    for _ in range(N):
        A, B, C = input().split()
        tree[A] = Node(A, B, C)

    tree['A'].preorder()
    print()
    tree['A'].inorder()
    print()
    tree['A'].postorder()
    print()