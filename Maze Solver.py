#Importing modules
import random

#Setting the parameters
iterations=10000
n=11
lr=0.8

#Initializing Q and reward matrix 
Q = [[0 for x in range(n)] for y in range(n)]
R = [[-1 for x in range(n)] for y in range(n)]
R[0][2]=R[0][4]=0
R[1][2]=0
R[2][0]=R[2][1]=R[2][7]=0
R[3][4]=0
R[4][0]=R[4][3]=R[4][9]=0
R[5][6]=0
R[6][5]=R[6][7]=0
R[6][10]=100
R[7][2]=R[7][6]=R[7][8]=0
R[8][7]=R[8][9]=0
R[9][4]=R[9][8]=0
R[9][10]=100
R[10][6]=R[10][9]=0
R[10][10]=100

#Training begins
for s in range(0,iterations):
    starter=[]
    for i in range(0,n):
        starter.append(chr(i+65))
    start=random.choice(starter)
    k=ord(start)-65
    randomizer_array=[]
    for j in range(0,n):
        if R[k][j]>-1:
            randomizer_array.append(j)
    next=random.choice(randomizer_array)
    largest=[]
    for x in range(0,n):
        if R[next][x]>-1:
            largest.append(Q[next][x])
    p=max(largest)
    Q[k][next]=R[k][next]+lr*p
    k=next
for i in range(0, n):
    for j in range(0, n):
        Q[i][j]=int(Q[i][j])

print('\nTrained Q matrix for the map is: \n')
for i in range(0, n):
    for j in range(0, n):
        print(Q[i][j],end=' ')
    print('\n'.strip())

#Testing
a=input('\nEnter the starting point: ')
print('How to get out: ',end='')
track=[]
u=ord(a)-65
print(a,end='')
print('->',end='')
while(u!=n-1):
    for j in range(0, n):
        if Q[u][j]>0:
            track.append(Q[u][j])
    t=max(track)
    tx=[]
    for y in range(0,n):
        if Q[u][y]==t:
            tx.append(y)
    tind=random.choice(tx)
    print(chr(tind+65),end='')
    u=tind
    if u==n-1:
        break
    else:
        print('->',end='')
print('\n')
