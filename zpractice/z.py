# f = open('io_file','w')
# f.write('Hello, world!')

# import os
# os.remove('C:\Users\nikhi\OneDrive\Desktop\foodapp\io_file')

class Student():
    age=23
    def __init__(self,name):
        self.name =  name
        print ( "in class,,,, ",self.name,"age ,,,,,,,, ",self.age )

s1 = Student('nik')
s2  = Student('nik2')

print(s1.age,'=====',s1.name)
print(s2.age , '======='+s2.name)
