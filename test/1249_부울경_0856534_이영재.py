from collections import deque
dx,dy=[0,0,-1,1],[1,-1,0,0]
for t in range(int(input())):
    c=int(input())
    maps=[list(list(map(int,input()))) for _ in range(c)]
    deep=[[999]*c for _ in range(c)]
    deep[0][0]=0
    a=0
    q=deque()
    q.append((0,0))
    while q:
        x,y=q.popleft()
        for i in range(4):
            tx,ty=x+dx[i],y+dy[i]
            if 0<=tx<c and 0<=ty<c:
                if deep[tx][ty]>deep[x][y]+maps[tx][ty]:
                    deep[tx][ty]=deep[x][y]+maps[tx][ty]
                    q.append((tx,ty))
    a=deep[-1][-1]
    print('#{} {}'.format(t+1, a))