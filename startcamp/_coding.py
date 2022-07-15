dx,dy=[0,0,-1,1],[1,-1,0,0]
for _ in range(10):
    t=input()
    maps=[list(list(map(int,input()))) for _ in range(16)]
    deep=[[0]*16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maps[i][j]==2:sx,sy=i,j
    q=[(sx,sy)]
    x=0
    while q:
        x,y=q.pop()
        for i in range(4):
            tx,ty=x+dx[i],y+dy[i]
            if 0<=tx<16 and 0<=ty<16:
                if maps[tx][ty]==3:
                    x=1
                    q=[]
                if maps[tx][ty]==0:
                    q.append((tx,ty))
    print('#{} {}'.format(t, x))

