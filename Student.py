class Student:

    def getdata(self,sname,rno):
        self.s=sname
        self.r=rno

    def putdata(self):
        print("Student Name : ",self.s)
        print("Roll No : ",self.r)

s1=Student()
s1.getdata("Harsh Amburkar",101)
s1.putdata()
