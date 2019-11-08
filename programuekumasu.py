tableno=7
members=71
turns=7
table=[[0 for i in range(turns)] for j in range(members)]

for i in range(1,members):
    tmp=table[i-1][0]
    if(1<=i<=10):
        table[i][0]=0
    elif(i%10==1):
        table[i][0]=i//10
    elif(tmp==6):
        table[i][0]=1
    else:
        table[i][0]=table[i-1][0]+1
print(table)
