a=int(input("请输入年份："))
if a%100==0:
    if a%400==0:
        print("yes")
    else:
        print("false")
elif a%4==0:
    print("yes")
else:
    print("false")


