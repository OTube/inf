for N in range(10000):
    B=bin(N)[2:]
    B=B.replace('0','2')
    B=B.replace('1','0')
    B=B.replace('2','1')
    R=int(B,2)
    if N-R==999:
        print(N)
        break
