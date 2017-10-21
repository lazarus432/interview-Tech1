class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def question5(ll, m):
    first = ll
    second = ll

    for i in range(0, m):
        if(first == None):
            return None
        else:
            first = first.next

    while(first != None):
        first = first.next
        second = second.next

    return second.data

a = Node(3)
b = Node(6)
c = Node(9)

a.next = b
b.next = c


print question5(a, 3)
print question5(b, 2)
print question5(c, 1)
