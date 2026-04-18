"""
Модуль для обходу бінарного дерева трьома основними способами.

Містить:
    - pre_order:  обхід у прямому порядку  (Вузол → Ліво → Право)
    - in_order:   обхід у симетричному порядку (Ліво → Вузол → Право)
    - post_order: обхід у зворотному порядку (Ліво → Право → Вузол)
"""
class Node:
    """
    Вузол бінарного дерева.

    Attributes:
        left:  лівий дочірній вузол
        right: правий дочірній вузол
        value: значення вузла
    """
    def __init__(self, data, left=None, right=None):
        """
        Ініціалізує вузол бінарного дерева.

        Args:
            L: лівий дочірній вузол (або None)
            R: правий дочірній вузол (або None)
            n: значення вузла
        """
        self.left = left
        self.right = right
        self.data = data
# Pre-order traversal
def pre_order(node):
    """
    Обхід дерева в прямому порядку: Вузол → Ліво → Право.

    Args:
        node: поточний вузол дерева

    Returns:
        список значень вузлів у порядку обходу
    """
    if node is None:
        return []
    value = [node.data]
    a = pre_order(node.left)
    b = pre_order(node.right)
    return value + a + b

# In-order traversal
def in_order(node):
    """
    Обхід дерева в симетричному порядку: Ліво → Вузол → Право.
    Для BST повертає елементи у відсортованому порядку.

    Args:
        node: поточний вузол дерева

    Returns:
        список значень вузлів у порядку обходу
    """
    if node is None:
        return []
    a = in_order(node.left)
    value = [node.data]
    b = in_order(node.right)
    return a + value + b

# Post-order traversal
def post_order(node):
    """
    Обхід дерева у зворотному порядку: Ліво → Право → Вузол.
    Корисний для видалення дерева або обчислення виразів.

    Args:
        node: поточний вузол дерева

    Returns:
        список значень вузлів у порядку обходу
    """
    if node is None:
        return []
    a = post_order(node.left)
    b = post_order(node.right)
    value = [node.data]
    return a + b + value
