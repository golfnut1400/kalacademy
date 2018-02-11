

class kalAcademy:

    teacher = 'Kal'

    def __int__(self,classNumber, className):
        self.classNumber = classNumber
        self.className = className

    def display(self):
        print("Class Number: ",self.classNumber)
        print("Class Name: ", self.className)
        print("Teacher: ", kalAcademy.teacher)


class1 = kalAcademy('001','Python 101')
print(kalAcademy.class1)

class2 = kalAcademy('002','Python 201')
print(class2)
