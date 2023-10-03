a=100
i=1
sum=0
while i<=10:
    s=a+a/2
    a=a/2
    i+=1
    sum=sum+s
print(f"第10次落地反弹的高度为：{a},总共经过{sum-a}米")

