a=str(input("请输入一个数字："))
b=a[::-1]
if a==b:
    print(f"{a} 是回文数")
else:
    print(f"{a}不是回文数")