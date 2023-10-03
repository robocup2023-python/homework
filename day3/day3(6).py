date=input("请输入年月日，格式为####-##-##")
a=int(date[0:4])
b=int(date[5:7])
c=int(date[8:9])
if a%100==0:
    if a%400==0:
        ms=[31,29,31,30,31,30,31,31,30,31,30,31]
if b%4==0:
    ms=[31,29,31,30,31,30,31,31,30,31,30,31]
else:
    ms=[31,28,31,30,31,30,31,31,30,31,30,31]
days=0
for i in range(1,13):
    if b==i:
        for j in range(i-1):
            days+=ms[j]
        print(days)
