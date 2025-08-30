class Query:
    def __init__(self, data=None):
        if data is None:
            data = []
        self.data=data
        self.len=len(self.data)
        self.sum=sum(self.data)

    def search(self,query):
        for i in range(self.len):
            if self.data[i]==query:
                return i
        return None
    def remove(self,query):
        q=self.search(query)
        if q is None:
            return False
        self.sum-=self.data[q]
        self.data=self.data[:q]+self.data[q+1:]
        self.len-=1

    def add(self,query):
        self.len+=1
        self.data.append(query)
        self.sum+=query
    def find(self,query):
        for i in range(self.len):
            l=[]
            if self.data[i] == query:
                l.append(i)
            if len(l)>0:
                return l
        return None
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
def combination(n,m):
    if n==0:
        return 1
    if m==0:
        return 1
    if n==m:
        return 1
    if n<m:
        return False
    return factorial(n)/factorial(n-m)/factorial(m)
def permutation(n,m):
    if n==0:
        return 1
    if m==0:
        return 1
    if n<m:
        return False
    return int(factorial(n)/factorial(n-m))
import sys
input = sys.stdin.readline
write = sys.stdout.write
s = 0
x = 0
def classify(q,target=None):
    global s,x
    if q==1:
        s+=target
        x^=target
    elif q==2:
        s-=target
        x^=target
    elif q==3:
        return s
    elif q==4:
        return x
    else:
        return False


n=int(input())
for i in range(n):
    m=input()
    if len(m)>2:
        m,k=map(int,m.split())
        classify(m,k)
    else:
        write(str(classify(int(m)))+'\n')

