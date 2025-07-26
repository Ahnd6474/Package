class Heap:
    def __init__(self,key=None,data=None):
        self.data=[float('inf')]
        self.len=0
        if key is None:
            key= lambda x,y: True if x>y else False
        self.key=key
        if data is not None:
            for i in data:
                self.insert(i)
    def __len__(self):
        return self.len
    def insert(self,d):
        if d in self.data:
            return
        self.len+=1
        self.data.append(d)
        self.up(self.len)


    def up(self,l):
        if self.key(self.data[l],self.data[(l//2)]):
            self.data[l//2],self.data[l]=self.data[l],self.data[l//2]
            self.up(l//2)
        else:
            return

    def delete(self):
        self.data[1]=float('-inf')
        self.down(1)


    def down(self,i):
        if 2*i+1<=self.len:
            if self.key(self.data[2*i],self.data[2*i+1]):
                self.data[i], self.data[2 * i] = self.data[2 * i], self.data[i]
                self.down(2*i)
            else:
                self.data[i], self.data[2 * i+1] = self.data[2 * i+1], self.data[i]
                self.down(2*i+1)
        elif 2*i<=self.len:
            self.data[i],self.data[2*i]=self.data[2*i],self.data[i]
            self.down(2*i)
        else:
            return

    def max(self):
        if self.len>0:
            return self.data[1] if self.data[1]!=float('-inf') else 0
        return 0
    def pop(self):
        t=self.max()
        if self.len>0:
            self.delete()
        return t
    def __str__(self):
        return str(self.data)


n=int(input())
h=Heap()
for i in range(n):
    t=int(input())
    if t>0: h.insert(t)
    else: print(h.pop())
