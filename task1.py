from collections import deque
class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        if parent!=None and isinstance(parent, Folder):
            parent.children.append(self)
        self.children = []

    def __str__(self) -> str:
        return self.name

    def path(self):
        res = str(self)
        node = self.parent
        while isinstance(node, Folder) and node!=None:
            res = str(node) +'\\' + res
            node = node.parent
        return res

class File:
    def __init__(self, name, extension, size, parent=None):
        self.name = name
        self.extension = extension
        self.size = size
        self.parent = parent
        if parent!=None and isinstance(parent, Folder):
            parent.children.append(self)

    def __str__(self) -> str:
        return self.name+'.'+self.extension

    def path(self):
        res = str(self)
        node = self.parent
        while isinstance(node, Folder) and node!=None:
            res = str(node) +'\\' + res
            node = node.parent
        return res

def explore(root: Folder):
    deq = deque()
    deq.append((0, root))
    while(len(deq)!=0):
        rank, node = deq.pop()
        print(rank, node)
        if isinstance(node, Folder):
            for child in node.children:
                deq.append((rank+1, child))

root = Folder("root", None)
folder = Folder("dir", root)
file = File("file", 'txt', 534, folder)
folder2 = Folder("bir", root)
explore(root)
print(file.path())