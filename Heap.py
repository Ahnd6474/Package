class Heap:
    def __init__(self, key=None, length=999999, data=None):
        self.data = [2**32] + [float('-inf')] * (length - 1)
        self.len = 0
        self.size=length
        if key is None:
            key = lambda x, y: x > y
        self.key = key
        if data is not None:
            for i in data:
                self.insert(i)

    def __len__(self):
        return self.len

    def insert(self, d):
        if self.len + 1 >= self.size:
            self.data.append(0)
            self.size+=1
        self.len += 1
        self.data[self.len] = d
        self.up(self.len)

    def up(self, l):
        while l > 1 and self.key(self.data[l], self.data[l // 2]):
            self.data[l], self.data[l // 2] = self.data[l // 2], self.data[l]
            l = l // 2

    def delete(self):
        if self.len == 0:
            return
        self.data[1] = self.data[self.len]
        self.len -= 1
        self.down(1)

    def down(self, i):
        while 2 * i <= self.len:
            left = 2 * i
            right = 2 * i + 1
            larger = left

            if right <= self.len and self.key(self.data[right], self.data[left]):
                larger = right

            if self.key(self.data[larger], self.data[i]):
                self.data[i], self.data[larger] = self.data[larger], self.data[i]
                i = larger
            else:
                break

    def max(self):
        return self.data[1] if self.len > 0 else 0

    def pop(self):
        if self.len == 0: return 0
        t = self.max()
        if self.len > 0:
            self.delete()
        return t

    def __str__(self):
        return str(self.data[1:self.len + 1])

import sys
input = sys.stdin.readline
write = sys.stdout.write

n = int(input())
h = Heap()
for i in range(n):
    t = int(input())
    if t > 0:
        h.insert(t)
    else:
        write(str(h.pop())+'\n')
