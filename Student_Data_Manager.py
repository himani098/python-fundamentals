class Student:
    def __init__(self, roll, name, age, marks):
        self.roll = roll
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Roll No : {self.roll}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Marks   : {self.marks}")
        print("-" * 25)


class StudentManager:
    def __init__(self):
        self.students = [] #self.students --> object of class StudentManager

        # self.students = [ Student(101,"Himani",20,89.5), Student(102,"Arya",21,95) ] --> after adding students

    # Add Student
    def add_student(self):
        roll = int(input("Enter Roll No: "))

        for s in self.students:
            if s.roll == roll:
                print("Roll number already exists!")
                return    #exits the add student method

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        student = Student(roll, name, age, marks)
        self.students.append(student)

        print("Student Added Successfully!")

    # Display Students
    def display_students(self):
        if len(self.students) == 0:
            print("No Records Found!")
            return

        print("\nStudent Records\n")

        for s in self.students:
            s.display()

    # Search Student
    def search_student(self):
        roll = int(input("Enter Roll No to Search: "))

        for s in self.students:
            if s.roll == roll:
                print("\nStudent Found\n")
                s.display()
                return

        print("Student Not Found!")

    # Update Student
    def update_student(self):
        roll = int(input("Enter Roll No to Update: "))

        for s in self.students:
            if s.roll == roll:
                s.name = input("Enter New Name: ")
                s.age = int(input("Enter New Age: "))
                s.marks = float(input("Enter New Marks: "))

                print("Record Updated Successfully!")
                return

        print("Student Not Found!")

    # Delete Student
    def delete_student(self):
        roll = int(input("Enter Roll No to Delete: "))

        for s in self.students:
            if s.roll == roll:
                self.students.remove(s)  #list.remove(element)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")


manager = StudentManager()

while True:

    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        manager.add_student()

    elif choice == 2:
        manager.display_students()

    elif choice == 3:
        manager.search_student()

    elif choice == 4:
        manager.update_student()

    elif choice == 5:
        manager.delete_student()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")


"""
composition (or object association):- 

no requirement of inheritance then 
Composition means one class contains objects of another class to perform its work.
It is called a Has-A relationship
here in this code --> StudentManager has a list of Student objects.
|-->student1 = Student()
|-->student2 = Student()
|-->manager.students.append(student1)
|-->manager.students.append(student2)

example :- 
class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine()    # Composition

    def drive(self):
        self.engine.start()
        print("Car Moving")

c = Car()
c.drive()


Object association simply means one object refers to another object.
car object ---> associated to --> engine object

composition --> Car HAS-A Engine
Inheritance --> Car IS-A Vehicle
"""