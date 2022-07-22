def in_order(x):
    c, rs = 0, [0,0]
    if x<=n:
        in_order(x*2)
        c += 1
        if x==1 : 
            rs[0] = c
        elif x==n//2 : 
            rs[1] = c
        in_order(x*2+1)
    return(c, rs)

t = int(input())
for i in range(t):
    n=int(input())
    in_order(1)