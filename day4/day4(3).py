x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[3,8,6],
   [2,4,6],
   [3,7,8]]
a=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j]=x[i][j]+y[i][j]
print(a)