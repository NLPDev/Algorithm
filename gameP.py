
pp=[]

tot=10

M=tot+10

for i in range(M):
    pp.append([0, 0])

pp[1][0]=1/3
pp[2][0]=1/3
pp[3][0]=1/3

# print(pp[1][1])
for i in range(M):
    for j in range(3):
        k=j+1
        if i>k:
            pp[i][0]=pp[i][0]+pp[i-k][1]/3
            # print("i={0}, k={1}, pp[i][0]={2}, pp[i-k][1]={3}".format(i, k, pp[i][0], pp[i-k][1]))

            pp[i][1] = pp[i][1] + pp[i-k][0] / 3


print(pp[tot][0]*100)