for a in range(int(input())):
    n,k=map(int,input().split())
    x=[list(map(int, input().split())) for _ in range(n)]
    z=0
    for i  in range(n):
        m=0
        for j in range(n):
            if x[i][j]==1:m+=1
            if x[i][j]==0 or j==n-1:
                if m==k:
                    z+=1
                m=0
        for j in range(n):
            if x[j][i]==1:m+=1
            if x[j][i]==0 or j==n-1:
                if m==k:
                    z+=1
                m=0
    print('#{} {}'.format(a+1,z))