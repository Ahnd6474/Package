import sys
input=sys.stdin.readline
write=sys.stdout.write

def pour(bucket_a,bucket_b):
    t=bucket_b[1]+bucket_a[1]
    bucket_b[1]=min(bucket_b[1]+bucket_a[1],bucket_b[0])
    bucket_a[1]=t-bucket_b[1]
    return bucket_a,bucket_b
l=[[0,0] for i in range(3)]
for i in range(3):
    l[i][0],l[i][1]=map(int,input().split())
for i in range(33):
    l[0],l[1]=pour(l[0],l[1])
    l[1],l[2]=pour(l[1],l[2])
    l[2], l[0]=pour(l[2],l[0])
l[0],l[1]=pour(l[0],l[1])
for i in range(3):
    print(l[i][1])
