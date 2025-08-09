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

def merge_sort(l):
    n=len(l)
    m=n//2
    if m<=0:
        return l
    l1=merge_sort(l[:m])
    l2=merge_sort(l[m:])
    n1,n2=len(l1),len(l2)
    r,p=0,0
    l=[]
    while r<n1 and p<n2:
        if l1[r]>l2[p]:
            l.append(l2[p])
            p+=1
        else:
            l.append(l1[r])
            r+=1
    l+= l1[r:]+l2[p:]
    return l
    
def quick_sort(l):
    n = len(l)
    if n <= 1:
        return l  # base case
    piv = l[0]
    r, p = 1, n - 1
    while r <= p:
        while r <= p and l[r] < piv:
            r += 1
        while r <= p and l[p] >= piv:
            p -= 1
        if r < p:
            l[r], l[p] = l[p], l[r]
    l[0], l[p] = l[p], l[0]
    return quick_sort(l[:p]) + [l[p]] + quick_sort(l[p+1:])


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

