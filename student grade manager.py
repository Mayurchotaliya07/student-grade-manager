class Student:
    Total_students = 0

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        Student.Total_students += 1

    @property
    def marks(self):
        return self._marks
    
    @marks.setter
    def marks(self, value):
        if 0 <= value <= 100:
            self._marks = value
        else:
            raise ValueError("Marks should be in between 0 to 100")
        
    def grade(self):
        if  80 <= self.marks <= 100:
            return "A"
        elif  60 <= self.marks < 80:
            return "B"
        elif 40 <= self.marks < 60:
            return "C"
        else:
            return "F"

    @classmethod
    def total_student(cls):
        print(f"Total {cls.Total_students} registered")
        
    @classmethod
    def from_string(cls, value):
        name, marks = value.split("-")
        return cls(name, int(marks))
    
    @staticmethod
    def passing_marks():
        return 40
    

s1 = Student("Mayur", 85)
s2 = Student("Ravi", 67)
s3 = Student("Neha", 42)
s4 = Student("Rohit", 25)

s5 = Student.from_string("Amit-78")

print(f"{s1.name}: Marks = {s1.marks}, Grade = {s1.grade()}")
print(f"{s2.name}: Marks = {s2.marks}, Grade = {s2.grade()}")
print(f"{s3.name}: Marks = {s3.marks}, Grade = {s3.grade()}")
print(f"{s4.name}: Marks = {s4.marks}, Grade = {s4.grade()}")
print(f"{s5.name}: Marks = {s5.marks}, Grade = {s5.grade()}")