list是可变的，因此倒序删除。
## 修改
list0=[1,2,3,4,5,6,7,8]
list=list0[::-1]
for i in list:
     if i%2! = 0:
     del list0[list0.index(i)]
print(list0)

     