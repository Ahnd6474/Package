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


