n,m = map(int, input().split())
org = []
mn = []
for _ in range(n):
    org.append(list(input()))
for x in range(n-8):
    for y in range(m-8):
        cnt = 0
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0 and org[i+x][j+y] == 'W' : cnt += 1
                if (i+j)%2 == 1 and org[i+x][j+y] == 'B' : cnt += 1
        mn.append(min(cnt, 64-cnt))
print(min(mn))