n=int(input())
begin=[0 for i in range(n)]
end=[0 for i in range(n)]
shift=[0 for i in range(n)]
for i in range(n):
    begin[i],end[i]=map(int,input().split())
    shift[i]=[j for j in range(begin[i],end[i])]
t=0
for i in range(n):
    s=set()
    for j in range(n):
        if j==i:
            continue
        s.update(shift[j])
    t=max(len(s),t)
print(t)
