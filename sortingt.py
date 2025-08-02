from Heap import Heap
import sys
input = sys.stdin.readline
write = sys.stdout.write

def hp_sort(l:[]):
    h=Heap(data=l, key = lambda x, y: x<y)
    for i in range(len(l)):
        write(str(h.pop())+'\n')
n = int(input())
l=[0]*n
for i in range(n):
    l[i]=int(input())
hp_sort(l)

def selection_sort(l,ret=False):
    n=len(l)
    for i in range(n):
        min=i
        for j in range(n-i):
            min= i+j if l[min]>l[i+j] else min
        l[i],l[min]=l[min],l[i]
    return l

import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
l=[0]*n
for i in range(n):
    l[i]=int(input())
l=selection_sort(l)
for i in l:
    write(str(i))
    write('\n')

