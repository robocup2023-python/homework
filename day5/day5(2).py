def a(lst):
    b=[]
    for i in range(len(lst)):
        if i%2!=1:
            b.append(lst[i])
    print(b)
a([8,3,5,9,2])
