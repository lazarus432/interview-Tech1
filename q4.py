

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def question4(root, n1, n2):
    if(root.value > n1 and root.value > n2):
        return question4(root.left, n1, n2)

    if(root.value < n1 and root.value < n2):
        return question4(root.right, n1, n2)

    return root

root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

n1 = 10; n2 = 14
t = question4(root, n1, n2)
print (n1, n2, t.value)

