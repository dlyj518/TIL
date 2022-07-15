dx,dy=[0,0,-1,1],[1,-1,0,0]
for _ in range(1):
    t=input()
    maps=[list(list(map(int,input()))) for _ in range(16)]
    deep=[[0]*16 for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maps[i][j]==2:sx,sy=i,j
    q=[(sx,sy)]
    z=0
    while q:
        x,y=q.pop()
        for k in range(4):
            tx,ty=x+dx[k],y+dy[k]
            if 0<=tx<16 and 0<=ty<16:
                if maps[tx][ty]==3:
                    z=1
                    q=[]
                if maps[tx][ty]==0 & deep[tx][ty]==0:
                    maps[x][y]=1
                    q.append((tx,ty))
        print(q,z)
    print('#{} {}'.format(t, z))