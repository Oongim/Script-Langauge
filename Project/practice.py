class Person:
    def __init__(self,name,phoneNumber):
        self.Name=name
        self.PhoneNumber=phoneNumber
    def PrintInfo(self):
        print("Info(Name: {0}, Phone Number: {1})".format(self.Name,self.PhoneNumber))
    def PrintPersonDate(self):
        print("Person(Name: {0}, Phone Number: {1})".format(self.Name, self.PhoneNumber))

class Student(Person):
    def __init__(self,name,phoneNumber,subject,studentID):
        Person.__init__(self,name,phoneNumber)
        self.Subject=subject
        self.StudentID=studentID

    def PrintStudentData(self):
        print("Student(Subject: {0}, Student ID: {1})".format(self.Subject, self.StudentID))


