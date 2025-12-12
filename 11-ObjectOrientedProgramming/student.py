# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.year=0

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.year=1
    student2.name = "Olivia"
    student2.age = 21
    student2.year=3
    student3.name="Weronika"
    student3.age=29
    student3.year=5

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old,{student1.year} year')
    print(f'{student2.name}, {student2.age} years old,{student2.year} year')
    print(f'{student3.name}, {student3.age} years old,{student3.year} year')

if __name__ == "__main__":
    main()