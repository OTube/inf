M=999999
for N in range(100000):
    B=bin(N)[2:]
    for i in range(3):
        S=sum(int(x) for x in str(int(B,2)))
        if S%2!=0:
            B+='1'
        else:
            B+='0'
    R=int(B,2)
    if R>1028:
        M=min(M,R)
print(M)
