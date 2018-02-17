import sys
class Library: #first class
    def __init__(self,list):#as it is visible we have _init_ constructor in all class
        self.list=list
    def Availaibility(self):
        print("0ur library has has following books")
        for book in self.list:
            print(book)
    def lend(self,requested):
        if requested in self.list:
            print("Please return book on time")
            self.list.remove(requested)
        else:
            print("The book is not available")
    def returned(self,retrn):
        self.list.append(retrn)

class Person:#2nd class
    def __init__(self,a):#_init_ constructor in second class
        self.A=a
    def RequestBook(self):
        p = int(input("Charges 5 for person,2 for student,0 for teachers :"))#private data member
        r=p+self.A
        if r==5:
            self.book=input("Enter the book you'd like to borrow : ")
            return self.book
        else:
            print("Pay the price that been asked according to type.")
    def ReturnBook(self):
        self.book=input("Enter the book you are returning :")
        return self.book
class Student(Person):#3rd class,inheriting from person class,super call constructor used
    def __init__(self,b,x):#_init_ constructor in third class
        b+=x
        Person.__init__(self,b)
class Teacher(Person):#4th class,inheriting from person class,mutiple inheritance
    def __init__(self,c,y):#_init_ constructor in fourth class
        c+=y
        Person.__init__(self,c)
class Librarian():#5th class
    def __init__(self,d,e):#_init_ constructor in fifth class
        self.D=d
        self.E=e
    def Authorize(self):#self is used in every class
        self.D=int(input("enter the librarian password : "))
        if self.D==3456:
            print("the password is authorized")
        else:
            print("sorry wrong password exiting...")
            sys.exit()



library=Library(["Throne Room","Tuders","Jack"])#instance of class 1
a=0
b=0
c=0
d=0
e=0
person=Person(a)#instance of class 2
student=Student(b,3)#instance of class 3
teacher=Teacher(c,5)#instance of class 4
librarian=Librarian(d,e)#instance of class 5
g=False
h=False
while h==False:
    print(""" ======ENTER MEMBER TYPE=======
                          1. Person
                          2. Student
                          3. Teacher
                          4. Quit
                          """)
    type=int(input("enter the chioce : "))
    if type==1:
        while g==False:
            print(""" ======LIBRARY MENU=======
                        1. Display books
                        2. Request book
                        3. Return book
                        4. Quit
                        """)
            choice=int(input("enter the choice : "))
            if choice==1:
                library.Availaibility()
            if choice==2:
                librarian.Authorize()
                library.lend(person.RequestBook())# implementing relationship between class 1 and 2
            if choice==3:
                librarian.Authorize()
                library.returned(person.ReturnBook())# implementing relationship between class 1 and 2
            if choice==4:
                print("going back to main menu....")
                break
    if type==2:
        while g==False:
            print(""" ======LIBRARY MENU=======
                        1. Display books
                        2. Request book
                        3. Return book
                        4. Quit
                        """)
            choice=int(input("enter the choice : "))
            if choice==1:
                library.Availaibility()
            if choice==2:
                librarian.Authorize()
                library.lend(student.RequestBook())# implementing relationship between class 1 and 3
            if choice==3:
                librarian.Authorize()
                library.returned(student.ReturnBook())# implementing relationship between class 1 and 3
            if choice==4:
                print("going back to main menu....")
                break
    if type==3:
        while g==False:
            print(""" ======LIBRARY MENU=======
                        1. Display books
                        2. Request book
                        3. Return book
                        4. Quit
                        """)
            choice=int(input("enter the choice : "))
            if choice==1:
                library.Availaibility()
            if choice==2:
                librarian.Authorize()
                library.lend(teacher.RequestBook())# implementing relationship between class 1 and 4
            if choice==3:
                librarian.Authorize()
                library.returned(teacher.ReturnBook())# implementing relationship between class 1 and 4
            if choice==4:
                print("going back to main menu....")
                break
    if type==4:
        sys.exit()
