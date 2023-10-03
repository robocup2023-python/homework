my_str="fhuidas 12`3'4"
alpha=0
space=0
digit=0
other=0
for i in my_str:
    if i.isalpha():
        alpha+=1
    elif i.isspace():
        space+=1
    elif i.isdigit():
        digit+=1
    else:
        other+=1
print(f"alpha={alpha},space={space},digit={digit},other={other}")