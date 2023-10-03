for i in range (100,1000):
    x=i//100
    y=i//10%10
    z=i%10
    if i==x*x*x+y*y*y+z*z*z:
        print(i)