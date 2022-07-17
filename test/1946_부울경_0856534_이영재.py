for i in range(int(input())):
    print('#'+str(i+1))
    t=''
    for j in range(int(input())):
        a,b=input().split()
        t+=a*int(b)
    for k in range(0,len(t),10):
        print(t[k:k+10])