"""
Модуль для видалення вузла з бінарного дерева пошуку (BST).

Містить:
    - TreeNode: клас вузла бінарного дерева
    - Solution: клас з методом видалення вузла з BST
"""
# Definition for a binary tree node.
class TreeNode:
    """
    Вузол бінарного дерева пошуку.

    Attributes:
        val:   значення вузла
        left:  лівий дочірній вузол (val < self.val)
        right: правий дочірній вузол (val > self.val)
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
    Містить методи для роботи з бінарним деревом пошуку.

    Methods:
        deleteNode: видаляє вузол з BST за заданим ключем
    """
    def deleteNode(self, root, key):
        """
        Видаляє вузол з BST за заданим ключем.

        Алгоритм:
        1. Рекурсивно обходить все дерево
        2. Якщо знайдено вузол з key:
           - немає лівого дочірнього → замінюємо правим
           - немає правого дочірнього → замінюємо лівим
           - є обидва → знаходимо найменший вузол у правому піддереві
             (інордер-наступник), копіюємо його значення, видаляємо його знизу

        Args:
            root: корінь дерева або піддерева
            key:  значення вузла для видалення

        Returns:
            корінь зміненого дерева
        """
        if root is None:
            return None
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        if root.val == key:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                probe = root.right
                while probe.left:
                    probe = probe.left
                root.val = probe.val
                root.right = self.deleteNode(root.right,probe.val)
        return root
