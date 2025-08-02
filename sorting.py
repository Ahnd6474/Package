from Heap import Heap
import sys
input = sys.stdin.readline
write = sys.stdout.write

def hp_sort(l:[]):
    h=Heap(data=l, key = lambda x, y: x<y)
    for i in range(len(l)):
        write(str(h.pop())+'\n')

def selection_sort(l,ret=False):
    n=len(l)
    for i in range(n):
        min=i
        for j in range(n-i):
            min= i+j if l[min]>l[i+j] else min
        l[i],l[min]=l[min],l[i]
    return l

def bubble_sort(l):
    n=len(l)
    for i in range(n):
        for j in range(n-1-i):
            if l[j+1]<l[j]:
                l[j+1],l[j]=l[j],l[j+1]
    return l

def insertion_sort(l):
    n=len(l)
    for i in range(n):
        t=l[i]
        c=i
        while c>0 and l[c-1]>=t:
            l[c]=l[c-1]
            c-=1
        l[c]=t
    return l
def counting_sort(l):
    d=[i for i in range(max(l)+1)]
    for i in l:
        d[i]+=1
    l=[]
    for i in range(len(d)):
        l+=[i]*d[i]
    return l


def comb_sort(l,s):
    n=len(l)
    gap=n
    while True:
        gap= int(gap//s) if gap//s>1 else 1
        c=0 if gap==1 else 1
        for i in range(n-gap):
            if l[i]>l[i+gap]:
                l[i],l[i+gap]=l[i+gap],l[i]
                c+=1
        if c==0:
            break
    return l
def main():
    import sys
    input = sys.stdin.readline
    write = sys.stdout.write
    
    n = int(input())
    l=[0]*n
    for i in range(n):
        l[i]=int(input())
    l=comb_sort(l,1.3)
    for i in l:
        write(str(i))
        write('\n')

