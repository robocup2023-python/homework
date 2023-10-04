class person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
per=person("名字","年龄","性别")

class student:
    def __init__(self,name,age,gender,classnumber,college):
        self.name=name
        self.age=age
        self.gender=gender
        self.classnumber=classnumber
        self.college=college
    def __str__(self):
        return f" 名字是{self.name},年龄是{self.age},性别是{self.gender},班号是{self.classnumber},学院是{self.college}"
stu=student("名字","年龄","性别","班号","学院")
print(stu)




