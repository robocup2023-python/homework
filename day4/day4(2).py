a=[1,3,5,7,9,0]
x=int(input("请输入一个数："))
if x>a[4]:
    a[5]=x
else:
    for i in range(len(a)):
        if a[i]>x:
            a.insert(i,x)
            break
print(a)


