a=[1,2,3,4,5,6,7,8]
x=int(input("请输入要提前的位数："))
for i in range(1,x+1):
    a.insert(0,a[7])
    a.pop(8)
    i+=1
print(a)