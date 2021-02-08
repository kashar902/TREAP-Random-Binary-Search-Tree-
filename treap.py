import random


class TreapNode:
    def __init__(self, key: int):
        self.key = key
        self.size = 1
        self.left = None
        self.right = None


class RandomizedBST:
    def __init__(self):
        self.root = None

    # Is the given tree Empty
    def Empty(self):
        if self.root == None:
            return 'Root is Empty'

    # Returns whether the given number is in the tree.
    def Member(self, t, k):
        if t is None:
            return False
        elif k < t.key:
            return self.Member(t.left, k)
        elif k > t.key:
            return self.Member(t.right, k)
        else:
            return True

    def member_1(self, k):
        return self.Member(self.root, k)

    # Gets the size of a (possibly Empty) tree.
    def Size(self, t):
        if t != None:
            return t.size
        return 0

    # Creates a new singleton tree with the given value.
    def New_Node(self, k):
        return TreapNode(k)

    # Sets the size of a node from the sizes of the immediate subtrees.
    def Fix_Size(self, t):
        t.size = 1 + self.Size(t.left) + self.Size(t.right)

    # Inserts a key as a leaf, returning the modified tree.
    # (This insertion operation will produce a severely imbalanced
    # tree if the keys are inserted in sorted order.)
    def LeafInsert(self, t, k):
        if t == None:
            return self.New_Node(k)
        elif k < t.key:
            t.left = self.LeafInsert(t.left, k)
            self.Fix_Size(t)
            return t
        elif k > t.key:
            t.right = self.LeafInsert(t.right, k)
            self.Fix_Size(t)
            return t
        else:
            return t

    # Performs a right rotation.
    # PRECONDITION: `d` and `d.left` are nodes
    def RotateRight(self, d):
        # b = d.left
        # d.left = b.right
        # b.right = d
        # self.Fix_Size(d)
        # self.Fix_Size(b)
        # return b
        d.left, d.right = d.right, d.left
        self.Fix_Size(d.right)
        self.Fix_Size(d.left)
        return d.left

    # Performs a left rotation.
    # PRECONDITION: `b` and `b.right` are nodes
    def RotateLeft(self, b):
        d = b.right
        b.right = d.left
        d.left = b
        self.Fix_Size(b)
        self.Fix_Size(d)
        return d
        # b.right, b.left = b.left, b.right
        # self.Fix_Size(b.left)
        # self.Fix_Size(b.right)
        # return b.right

    # Inserts an element at the root, returning the modified tree.
    # (This insertion operation will produce a severely imbalanced
    # tree if the keys are inserted in sorted order.)
    def RootInsert(self, t, k):
        if t == None:
            return self.New_Node(k)
        elif k < t.key:
            t.left = self.RootInsert(t.left, k)
            return self.RotateRight(t)
        elif k > t.key:
            t.right = self.RootInsert(t.right, k)
            return self.RotateLeft(t)
        else:
            return t

    # Inserts an element, maintaining randomness and returning the modified tree.
    def insert_1(self, t, k):
        if t == None:
            return self.New_Node(k)
        elif random.randint(0, self.Size(t) + 1) == 0:
            return self.RootInsert(t, k)
        elif k < t.key:
            t.left = self.insert_1(t.left, k)
            self.Fix_Size(t)
            return t
        elif k > t.key:
            t.right = self.insert_1(t.right, k)
            self.Fix_Size(t)
            return t
        else:
            return t

    def insert(self, k):
        self.root = self.insert_1(self.root, k)

    # Joins two trees, assuming all the keys of the first are less than
    # all the keys of the second.
    def Join(self, tree_1, tree_2):
        if tree_1 == None:
            return tree_2
        elif tree_2 is None:
            return tree_1
        elif random.randint(0, self.Size(tree_1) + self.Size(tree_2)) < self.Size(tree_1):
            tree_1.right = self.Join(tree_1.right, tree_2)
            self.Fix_Size(tree_1)
            return tree_1
        else:
            tree_2.left = self.Join(tree_1, tree_2.left)
            self.Fix_Size(tree_2)
            return tree_2

    # Deletes an element from a tree, returning the modified tree.
    def Delete(self, t, k):
        if t == None:
            return t
        elif k < t.key:
            t.left = self.Delete(t.left, k)
            self.Fix_Size(t)
            return t
        elif k > t.key:
            t.right = self.Delete(t.right, k)
            self.Fix_Size(t)
            return t
        else:
            return self.Join(t.left, t.right)

    def Del(self, k):
        self.root = self.Delete(self.root, k)

    # Returns the Height (max depth) of a tree.
    def Tree_Height(self, t):
        if t == None:
            return 0
        else:
            return 1 + max(self.Tree_Height(t.left), self.Tree_Height(t.right))

    def Height(self):
        return self.Tree_Height(self.root)

    # Pretty-prints a tree.
    def PrintTree(self, t='none', n_spaces=0):
        if t == 'none':
            t=self.root
        if t is None:
            return
        print(" " * n_spaces, 'key:', t.key, 'size:', t.size, 'Height:', self.Tree_Height(t))
        self.PrintTree(t.left, n_spaces + 2)
        self.PrintTree(t.right, n_spaces + 2)


# Builds a random tree of `n` elements, using `f` to produce each element
def sample(n, f):
    result = RandomizedBST()
    for i in range(10):
        result.insert(f(i))
    result.PrintTree()
if __name__ == '__main__':
    sample(100, lambda y: y)

