from calendar import c


def st(r):
    global c
    c += 1
    for i in tr[int(r)]:
        if i:st(i)
    return c

for t in range(int(input())):
    e,n = map(int,input().split())
    nd = list(map(int,input().split()))
    tr=[[] for _ in range(e+2)]
    for i in range(0,e*2,2):
        tr[nd[i]].append(nd[i+1])
        c=0
    print(f'#{t+1} {st(n)}')
