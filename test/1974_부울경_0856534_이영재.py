def prod(x):
    a=1
    for i in x:
       a*=i
    return a
 
for i in range(int(input())):
    x=[list(map(int, input().split())) for _ in range(9)]
    z=1
    for j in range(3):
        for k in range(3):
            l=3*j+k
            z-=1 if sum(x[l])!=45 else 0
            z-=1 if sum([k[l] for k in x])!=45 else 0
            z-=1 if prod(x[l])!=362880 else 0
            z-=1 if prod([k[l] for k in x])!=362880 else 0
            z-=1 if sum(sum([y[j*3:j*3+3] for y in x[k*3:k*3+3]],[]))!=45 else 0
            z-=1 if prod(sum([y[j*3:j*3+3] for y in x[k*3:k*3+3]],[]))!=362880 else 0
            z=0 if z!=1 else 1
    print('#'+str(i+1)+' '+str(z))