from Heap import Heap
import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
l=[0]*n
for i in range(n):
    l[i]=int(input())
hp_sort(l)
