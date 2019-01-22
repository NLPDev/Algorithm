
M=10010

def find(pos):
    pos[0]=0
    pos[1]=1
    pos[2] = 1
    pos[3] = 1
    pos[4] = 0
    pos[5] = 1
    pos[6] = 1
    pos[7] = 1

    for i in range(8, M):
        if pos[i-1]==0 or pos[i-3]==0 or pos[i-4]==0:
            pos[i]=1
        else:
            pos[i]=0





pp=[]
tot=10000

M=tot+1
for i in range(M):
    pp.append(0)


find(pp)

if pp[tot]==0:
    print("Lost")
else:
    print("Win")