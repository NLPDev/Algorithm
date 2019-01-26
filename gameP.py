#  pp[i][0]: the probability that player1 will take the ith
#  pp[i][1]: the probability that player2 will take the ith

#  Player1 start the game, so pp[0][1]=1

pp=[]

tot=10000

M=tot+10

for i in range(M):
    pp.append([0, 0])

pp[0][1]=1 #initialize

for i in range(M):
    for j in range(3):
        k=j+1
        if i>=k:
            pp[i][0]=pp[i][0]+pp[i-k][1]/3

            pp[i][1] = pp[i][1] + pp[i-k][0] / 3


print("The probability Player1 will be winner : {} % ".format(pp[tot][0]*100))