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
    lis = []
    max_rank = 0
    while(len(deq)!=0):
        rank, node = deq.pop()
        max_rank = max(max_rank, rank)
        if node!= root: lis.append((rank, node))
        ##print(rank, node)
        if isinstance(node, Folder):
            for child in node.children:
                deq.append((rank+1, child))
                
    le = len(lis)
    
    row = [0 for _ in range(max_rank)]
    for i in range(le):
        rank, item = lis[i]
        if rank==1:
            print("found")
            row[0] = i+1
    print()
    print(root)
    for i in range(le*2):
        line = ''
        j = i//2
        if i%2 == 1:
            rank, item = lis[j]
            for k in range(len(row)):
                if k==rank-1:
                    line += "+---"
                    break
                elif j<row[k]:
                    line += '|   '
                else:
                    line += '    '
            line+=str(item)
            if isinstance(item, Folder) and len(item.children)>0:
                upper_bound = 0
                lower_rank = rank+1
                for v in range(j+1, len(lis)):
                    rank_v, item_v = lis[v]
                    if rank_v==lower_rank:
                        upper_bound = v+1
                    if rank_v<=rank:
                        break
                row[rank] = upper_bound
        else:
            for k in range(max_rank):
                line += '|   ' if j<row[k] else '    '
        print(line)
    print(row)

root = Folder("root", None)
folder3 = Folder('tir', root)
folder2 = Folder("bir", root)
folder4 = Folder("hp", folder2)
folder = Folder("dir", folder2)
file = File("file", 'txt', 534, folder)
explore(root)
print(file.path())