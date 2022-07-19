def spin(a,n):
    x=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            x[i][j]=a[n-j-1][i]
    return(x)
 
for i in range(int(input())):
    print('#'+str(i+1))
    n=int(input())
    a=[list(map(int, input().split())) for _ in range(n)]
    a9=spin(a,n)
    a1=spin(a9,n)
    a2=spin(a1,n)
    for j in range(n):
        for k in range(n):
            print(a9[j][k], end='')
        print(end=' ')
        for k in range(n):
            print(a1[j][k], end='')
        print(end=' ')
        for k in range(n):
            print(a2[j][k], end='')
        print()