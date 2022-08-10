def ms(ls):
    l = len(ls)
    if l < 2 : return ls
    lf = ms(ls[:l//2])
    rt = ms(ls[l//2:])
    i,j = 0,0
    mg=[]
    while i<l//2 and j<(l-l//2):
        if lf[i]<rt[j] : mg.append(lf[i]); i += 1
        else: mg.append(rt[j]); j += 1
    mg += lf[i:]
    mg += rt[j:]
    return mg

x=[]
for i in range(int(input())):
    x.append(int(input()))
print(ms(x))
