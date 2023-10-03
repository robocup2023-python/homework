a=int(input("输入要相加的数："))
b=int(input("输入要相加的个数："))
sum=0
for i in range(1,b+1):
    sum=sum+a
    a = a + a * 10 * i
print(sum)
