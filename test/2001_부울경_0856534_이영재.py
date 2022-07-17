for a in range(int(input())):
    n,m=map(int,input().split())
    x=[list(map(int, input().split())) for _ in range(n)]
    mx=0
    for i in range(n-m+1):
        for j in range(n-m+1):
            s=sum(sum([y[j:j+m] for y in x[i:i+m]],[]))
            mx=s if s>mx else mx
    print('#{} {}'.format(a+1,mx))