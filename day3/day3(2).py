x=int(input("请输入一个奇数："))
a=x//2+1
for i in range(1,a+1):
    print(('*'*(2*i-1)).center(x))
j=a
while j>=1:
    print(('*'*(2*j-1)).center(x))
    j-=1
