def recur(node, a):
    a.append(node.NodeValue)
    for child in node.Children:
        recur(child, a)
    return a


def findn(node, val, a):
    if node.NodeValue == val:
        a.append(node)
    for child in node.Children:
        findn(child, val, a)
    return a


def countn(node):
    k = 1
    for child in node.Children:
        k += countn(child)
    return k


class SimpleTreeNode:
    def __init__(self, val, parent):
        self.NodeValue = val  # значение в узле
        self.Parent = parent  # родитель или None для корня
        self.Children = []  # список дочерних узлов


class SimpleTree:
    def __init__(self, root):
        self.Root = root  # корень, может быть None

    def AddChild(self, ParentNode, NewChild):
        if ParentNode is not None:
            ParentNode.Children.append(NewChild)
            NewChild.Parent = ParentNode

    def DeleteNode(self, NodeToDelete):
        if NodeToDelete == self.Root:
            self.Root = None
            return

        if NodeToDelete.Parent is not None:
            NodeToDelete.Parent.Children.remove(NodeToDelete)

        NodeToDelete.Children = []
        NodeToDelete.Parent = None

    def GetAllNodes(self):
        if self.Root is None:
            return []
        return recur(self.Root, [])

    def FindNodesByValue(self, val):
        if self.Root is None:
            return []
        return findn(self.Root, val, [])

    def Count(self):
        if self.Root is None:
            return 0
        return countn(self.Root)


root = SimpleTreeNode(0, None)
tree = SimpleTree(root)

n1 = SimpleTreeNode(1, root)
n2 = SimpleTreeNode(2, root)
n3 = SimpleTreeNode(3, n1)
n4 = SimpleTreeNode(4, n2)
tree.AddChild(root, n1)
tree.AddChild(root, n2)
tree.AddChild(n1, n3)
tree.AddChild(n2, n4)

print(tree.GetAllNodes())
print(tree.FindNodesByValue(3))
print("Количество узлов:", tree.Count())
tree.DeleteNode(n4)
print(tree.GetAllNodes())
print("Количество узлов:", tree.Count())
