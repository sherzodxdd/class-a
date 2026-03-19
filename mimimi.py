class Student:
    ism = "Farhod"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self, kurs_nomi):
        self.kurs_nomi = kurs_nomi
        return f"Mening ismim {self.ism}, men {self.age} yoshdaman, biz {self.kurs_nomi} o'qiman"


ism = "Farhod"

Student1 = Student("Farhod", 18)
print(Student1.info("Python"))