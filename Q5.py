class Student:
    def __init__(self,name,section):
        self.name=name
        self.section=section

    def get_name(self):
        return self.name

    @classmethod
    def get_obj_from_string(cls, inp):
        name, section = inp.split("-")
        return cls(name, section)

student_1 = Student.get_obj_from_string("name-A")
print(student_1.__dict__)
