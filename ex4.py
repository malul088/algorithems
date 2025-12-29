import random
from typing import Optional

def partition(a, l, r, key):
    x=a[r]
    i=l-1
    for j in range(l, r):
        if key(a[j]) <= key(x):
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[r]=a[r],a[i+1]
    return i+1


# finds the kth value
def quick_kth(arr, l, r, k, key = lambda x: x):
    if k < 1 or k > r - l + 1:
        raise ValueError("k is out of bounds")
    index = partition(arr, l, r, key)
    # if position is same as k
    if index - l == k - 1:
        return arr[index]
    # If position is more, recur left
    if index - l > k - 1:
        return quick_kth(arr, l, index - 1, k, key)
    # Else recur right
    return quick_kth(arr, index + 1, r, k - (index - l + 1), key)


class Node:
    def __init__(self, value):
        self.value = value
        # count removed — not used anymore
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
        self.parent: Optional[Node] = None


class Tree:
    def __init__(self, key=lambda x: x):
        self.root = None
        self.key = key  # not used yet in the tree

    def insert(self, value):
        x = self.root
        y: Optional[Node] = None
        while x is not None:
            if self.key(value) == self.key(x.value):
                # if the value is already in the tree, ignore
                return
            y = x
            if self.key(value) > self.key(x.value):
                x = x.right
            else:
                x = x.left

        new_node = Node(value)
        if y is None:
            # the tree was empty
            self.root = new_node
            return
        assert (self.key(value) != self.key(y.value))
        if self.key(value) > self.key(y.value):
            y.right = new_node
        else:
            y.left = new_node
        new_node.parent = y



arr1 = [7, 2, 1, 6, 8, 5, 3]
result1 = quick_kth(arr1, 0, len(arr1) - 1, 3)
print(f"האיבר ה-{3} הקטן ביותר הוא:", result1)

result1 = quick_kth(arr1, 0, len(arr1) - 1, 7)
print(f"האיבר ה-{7} הקטן ביותר הוא:", result1)