from collections import deque
class Folder:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        if isinstance(parent, Folder):
            parent.children.append(self)
        self.children = []

    def __str__(self) -> str:
        return self.name

    def path(self):
        res = str(self)
        node = self.parent
        while isinstance(node, Folder):
            res = str(node) +'\\' + res
            node = node.parent
        return res

class File:
    def __init__(self, name, extension, size, parent=None):
        self.name = name
        self.extension = extension
        self.size = size
        self.parent = parent
        if isinstance(parent, Folder):
            parent.children.append(self)

    def __str__(self) -> str:
        return self.name+'.'+self.extension

    def path(self):
        res = str(self)
        node = self.parent
        while isinstance(node, Folder):
            res = str(node) +'\\' + res
            node = node.parent
        return res

def dfs_list(root: Folder):
    deq = deque()
    deq.append((0, root))
    lis = []
    max_rank = 0
    while len(deq)!=0:
        rank, node = deq.pop()
        max_rank = max(max_rank, rank)
        if node!= root:
            lis.append((rank, node))
        ##print(rank, node)
        if isinstance(node, Folder):
            for child in node.children:
                deq.append((rank+1, child))

    return lis

def fill_row(index, rank, row, node_lis):
    upper_bound = 0
    lower_rank = rank+1
    for i in range(index+1, len(node_lis)):
        rank_v = node_lis[i][0]
        if rank_v==lower_rank:
            upper_bound = i+1
        if rank_v<=rank:
            break
    row[rank] = upper_bound

def tree_presentation(root: Folder):
    lis = dfs_list(root)
    length = len(lis)
    max_rank = max(lis, key=lambda e: e[0])[0]
    row = [0 for _ in range(max_rank)]
    for i in range(length):
        rank = lis[i][0]
        if rank==1:
            row[0] = i+1

    res = str(root)+'\n'
    for j in range(length):
        #blank line above node
        line = ''
        for k in range(max_rank):
            line += '|   ' if j<row[k] else '    '
        res += line.rstrip()+'\n'
        #line with node
        line = ''
        rank, item = lis[j]
        for k in range(max_rank):
            if k==rank-1:
                line += "+---"
                break
            if j<row[k]:
                line += '|   '
            else:
                line += '    '
        line+=str(item)
        res+=line+'\n'
        #writing info for next iterations
        if isinstance(item, Folder) and len(item.children)>0:
            fill_row(j, rank, row, lis)

    return res

korin = Folder("root", None)
tir = Folder('tir', korin)
hp = Folder("hp", korin)
bir = Folder("bir", korin)
jir = Folder("jir", bir)
file = File("file", 'txt', 534, jir)
rir = Folder('rir', tir)
print(tree_presentation(korin))
