for i in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
    if n>m:
        for j in range(n-m+1):
            x=0
            for k in range(m):x+=a[k+j]*b[k]
            l.append(x)
    else:
        for j in range(m-n+1):
            x=0
            for k in range(n):x+=a[k]*b[k+j]
            l.append(x)
    print('#'+str(i+1)+' '+str(max(l)))