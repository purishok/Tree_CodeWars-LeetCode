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
