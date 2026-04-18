"""
Модуль для обходу бінарного дерева за рівнями.

Містить:
    - tree_by_levels: повертає список елементів дерева, відсортованих за рівнями
"""
class Node:
    """
    Вузол бінарного дерева.

    Attributes:
        left:  лівий дочірній вузол
        right: правий дочірній вузол
        value: значення вузла
    """
    def __init__(self, l, r, n):
        """
        Ініціалізує вузол бінарного дерева.

        Args:
            L: лівий дочірній вузол (або None)
            R: правий дочірній вузол (або None)
            n: значення вузла
        """
        self.left = l
        self.right = r
        self.value = n
def tree_by_levels(node):
    """
    Returns a list of tree elements sorted by levels (BFS order).

    Traverses the tree recursively, grouping nodes by their depth
    level in a dictionary, then flattens it into a list.

    Args:
        node: root of the binary tree

    Returns:
        list of node values sorted by levels, or [] if root is None
    """
    tree_dict = {}
    def recurs(tree, level):
        if tree is None:
            return
        tree_dict.setdefault(level,[]).append(tree.value)
        recurs(tree.left, level + 1)
        recurs(tree.right, level + 1)
    recurs(node, 0)
    result = []
    for level in sorted(tree_dict):
        result.extend(tree_dict[level])
    return result
