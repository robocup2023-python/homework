import os
import random
import string
if not os.path.exists("img"):
    os.mkdir("img")
for i in range (100):
    filename=''.join(random.choices(string.ascii_letters+string.digits,k=4))+".png"
    with open(os.path.join("img",filename),"w") as f:
        f.write("file")
print("down")

