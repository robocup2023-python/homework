file=open('test.txt.','a')
lines=file.readlines()
for i in range(len(lines)):
    lines[i]=lines[i].strip()+'3.m\n'
file.close()
file=open('test.txt.','w')
file.writelines(lines)
file.close()