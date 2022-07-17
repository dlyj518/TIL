for i in range(int(input())):
    n=input()
    if n==n[::-1]:a='1'
    else: a='0'
    print('#'+str(i+1)+' '+a)