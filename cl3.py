courses = []


class subject:

    def __init__(self, name, code, specialty, creditss, ects):
        self.creditss = creditss
        self.ects = ects
        self.speciality = specialty
        self.code = code
        self.name = name

    def str(self):
        return "\n Subject name: " + self.name + "\n Subject code: " + self.code + "\n Subject speciality: " + self.speciality + "\n Subject credits: " + self.creditss + "\n Subject ects: " + self.ects


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def repr(self):
        return "Person's name: " + self.name + "Person's surname" + self.surname + "Person's age: " + self.age

    def init(self, name, surname, age):
        pass


class Instructor(Person):
    def __init__(self, name, surname, age, idn, email, coursess):
        super().__init__(name, surname, age)
        self.email = email
        self.courses = coursess
        self.name = name
        self.idn = idn

    def repr(self):
        return " " + self.name


class Student(Person):
    def __init__(self, name, surname, age, course, speciality, registered_courses):
        super().__init__(name, surname, age)
        self.course = course
        self.speciality = speciality
        self.registered_courses = registered_courses

    def repr(self):
        return "Person's name: " + self.name + "Person's surname" + self.surname + "Person's age: " + self.age + self.course


class Manager:

    @staticmethod
    def addc():
        name = input("name: ")
        code = input("code: ")
        specialty = input("speciality: ")
        creditss = input("cr: ")
        ects = input("ects: ")
        a = subject(name, code, specialty, creditss, ects).str()
        courses.append(a)
        for i in range(len(courses)):
            print(courses[i])
        return ''

    @staticmethod
    def addp():
        name = input("name: ")
        surname = input("surname: ")
        age = input("age: ")
        a = Person(name, surname, age).repr()
        return a

    while True:
        print("Options: \n1.Add courses\n2.Add person")
        while True:
            check = input("Please, enter the number of the option: ")
            if check == '1':
                print(addc())
                break
            elif check == '2':
                print(addp())
                break
            else:
                exit()
        if int(check) > 2:
            exit()
