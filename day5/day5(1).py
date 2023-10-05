def cacaluate(lst):
    b=[]
    b.insert(0,sum(lst)/len(lst))
    for i in lst:
        if i>b[0]:
            b.append(i)
    print(b)
cacaluate([1,2,3,4,5])

