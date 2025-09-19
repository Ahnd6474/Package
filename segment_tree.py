from math import log2, ceil
class SegmentTree:
    def __init__(self, entry:int,data,key=None):
        entry=2**ceil(log2(entry))
        self.entry=entry
        self.len=2*entry
        if key==None:
            key = lambda x,y:x+y
        self.key=key
        if len(data)!=entry:
            data+=[0]*(entry-len(data))
        self.tree=[0 for i in range(entry)]+data

    @tree.setter
    def tree(self,tree):
        for i in range(self.entry,0,-1):
            tree[i]=self.key(tree[2*i],tree[2*i+1])
        return tree

    

