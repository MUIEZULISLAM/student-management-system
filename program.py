class Student:
    file_name = "program.txt"
    students = []

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        Student.students.append(self)

    def show_self(self):
        print(f"{self.name}|{self.age}|{self.marks}")

    def object_to_file_format(self):
        return f"{self.name},{self.age},{self.marks}\n"

    def save_to_file(self):
        with open(Student.file_name, "a") as f:
            f.write(self.object_to_file_format())

    @classmethod
    def re_write_file(cls):
        with open(Student.file_name, "w") as f:
            for stu in cls.students:
                f.write(stu.object_to_file_format())

    @classmethod
    def load_the_file(cls):
        cls.students.clear()
        try:
            with open(cls.file_name, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    name, age, marks = line.split(",")
                    cls(name, int(age), int(marks))
        except FileNotFoundError:
            pass

    @classmethod
    def show_all(cls):
        for stu in cls.students:
            stu.show_self()
        if not cls.students:
            print("no data found!")


def student_intake():
    while True:
        student_name = input("enter name of student: ").strip().lower()
        if student_name == "no":
            break
        student_age = int(input("enter age of student: "))
        student_marks = int(input("enter marks of student: "))
        stu = Student(student_name, student_age, student_marks)
        stu.save_to_file()


def search_the_student():
    student_name = input("enter name of student: ").strip().lower()
    found = False
    for stu in Student.students:
        if stu.name == student_name:
            found = True
            stu.show_self()
            break
    if not found:
        print("such student dont exsist in our record")


def update_the_student():
    student_name = input("enter name of student: ").strip().lower()
    factor = input("enter thing name to update e.g age,marks: ").strip().lower()
    found = False

    if factor == "marks":
        for stu in Student.students:
            if stu.name == student_name:
                found = True
                update_marks = int(input("enter total marks to update: "))
                stu.marks = update_marks
                Student.re_write_file()
                print("student updated successfully")
                break
        if not found:
            print("no such student exsist to update")

    elif factor == "age":
        for stu in Student.students:
            if stu.name == student_name:
                found = True
                new_age = int(input("enter new age: "))
                stu.age = new_age
                Student.re_write_file()
                print("student updated successfully")
                break
        if not found:
            print("no such student exsist to update")

    else:
        print("invalid option!")


def remove_the_student():
    student_name = input("enter name of student to remove: ").strip().lower()
    found = False
    for stu in Student.students:
        if stu.name == student_name:
            found = True
            Student.students.remove(stu)
            Student.re_write_file()
            print("student removed successfully")
            break
    if not found:
        print("no such student exsist to remove!")


def show_all_students():
    Student.show_all()


def total_check():
    total = {}
    for stu in Student.students:
        if stu.name in total:
            total[stu.name] += stu.marks
        else:
            total[stu.name] = stu.marks

    for student, marks in total.items():
        print(f"{student} has total marks of {marks}!")

    if not total:
        print("no record found")


def main():
    Student.load_the_file()   
    while True:
        print("1.add student")
        print("2.show all students")
        print("3.update student")
        print("4.remove student")
        print("5.view student by name")
        print("6.check students total record")
        print("7.quit")

        option = input("enter your desire option: ")

        if option == "1":
            student_intake()
        elif option == "2":
            show_all_students()
        elif option == "3":
            update_the_student()
        elif option == "4":
            remove_the_student()
        elif option == "5":
            search_the_student()
        elif option == "6":
            total_check()
        elif option == "7":
            print("program exited")
            break
        else:
            print("invalid option")


main()


            










        