# # MULTIPLE INHERITANCE QUESTIONS
# # 1. Create two classes Father and Mother with methods 
# # skills_father() and skills_mother(). Create a
# # child class Child that inherits from both and prints
# #  both skills.
# class Father:
#     def skills_father(self):
#         print('skills father')
# class Mother:
#     def skills_mother(self):
#         print('skills mother')
# class Child(Father,Mother):
#     def skills_child(self):
#         print('this child is sepcial')
# obj=Child()
# obj.skills_child()
# obj.skills_father()
# obj.skills_mother()
# # 2. Write a program where class Teacher has a method teach() and 
# # class Researcher has a method
# # research(). Create a class Professor that inherits from both
# #  and uses both methods.
# class Teacher:
#     def teach(self):
#         print('teach')
# class Researcher:
#     def research(self):
#         print('research')
# class Professor(Teacher,Researcher):
#     def display(self):
#         print('prof')
# obj=Professor()
# obj.research()
# obj.display()
# # 3. Create two classes Engine and ElectricSystem with respective
# #  methods. Create a class
# # HybridCar that inherits from both and demonstrates both
# #  functionalities.
# class Engine:
#     def display1(self):
#         print('engine of the car')
# class Electric:
#     def display2(self):
#         print('electric')
# class Hybrid(Engine,Electric):
#     def display(self):
#         print('modify')
# obj=Hybrid()
# obj.display2()
# 4. Implement two classes Writer and Speaker with methods
#  write() and speak(). Create a class
# # Author that inherits from both and calls both methods.
# class Writer:
#     def write(self):
#         print('who can write')
# class Speaker:
#     def speak(self):
#         print('who can speak')
# class Author(Writer,Speaker):
#     def display(self):
#         print(f'who can do both {self.write()},{self.speak()}')
# obj=Author()
# obj.display()

# # 5. Create two parent classes Calculator1 (addition) and 
# # Calculator2 (multiplication). Create a child
# # class that uses both operations.
# class Cal1:
#     def add(self,a,b):
#          return a+b
    
# class Cal2:
#     def sub(self,a,b):
#           return a-b
        
# class Cal3(Cal1,Cal2):
#     def display(self,a,b):
#         print(f'the calculatiion of a and b is in add {a+b},and sub {a-b}')
# obj=Cal3()
# obj.display(4,6)

# 6. Demonstrate method overriding in multiple inheritance
#  where both parent classes have a method
# with the same name.
# class Parent1:
#     def display(self):
#         print("Display from Parent1")

# class Parent2:
#     def display(self):
#         print("Display from Parent2")

# class Child(Parent1, Parent2):
#     pass
#     # def display(self):
#     #     print("Display from Child")
# obj = Child()
# obj.display()
# # 7. Create a class A and B with constructors. Create class C inheriting from both and show how
# # constructors are called.
# class A:
#     def __init__(self):
#         print("Constructor of class A")
# class B:
#     def __init__(self):
#         print('constructor of b')
# class C(A,B):
#     def display(self):
#         print(f'this is show of A AND  B')
# obj=C()
# obj.display()
# # 8. Write a program to demonstrate the Method Resolution Order
# #  (MRO) in multiple inheritance.
# class A :
#     def __init__(self):
#         print('a')
# class B:
#     def __init__(self):
#         print('b')
# class C(A,B):
#     def display(self):
#         print('c')
# obj=C()
# print(C.__mro__)
#     # 9. Create two classes Person and Employee with attributes.
#     #  Inherit both into Manager and display
# # combined details.
# class Person:
#     def display2(self,age):
#         self.age=age
# class Employee:
#     def display1(self,name):
        
#         self.n=name
# class Manager( Person, Employee):
#     def display(self, name,age):
#         name. __init__(name)
#         age. __init__(age)
#         print(age,name)
# obj=Manager()
# obj.display('jATIN',45)
# # 10. Implement a class SmartDevice that inherits from both Phone
# #  and Camera and performs both
# # calling and clicking photos.
# class Phone:
#     def displau(self):
#         A='this is phone'
#         return A
# class Camera:
#     def displaus(self):
#         b='this is camera'
#         return b 
# class Smartdevice(Phone,Camera):
#     def display(self):
#         print(f'smart device property {self.displau()} and {self.displaus()}')
# obj=Smartdevice()
# obj.display()
# MULTILEVEL INHERITANCE QUESTIONS
# 1. Create class Grandparent, Parent, and Child. 
# Add methods in each and show how child
# accesses all.
# class Grandparents:
#     def dis(self,gotra):
#         self.gotra=gotra
#         print('gorta is : ',self.gotra)
# class  Father(Grandparents):
#     def dis2(self,gotra,jamen):
#         super().dis(gotra)
#         self.jamen=jamen
#         print('jamen is :',self.jamen)
# class  Child(Father):
#     def dis3(self,name,jamen,gotra):
#         super().dis2(gotra,jamen)
#         self.name=name
#         print('name is : ',self.name)
# # obj=Child()
# # obj.dis3('jatin',0,'mulani')
# # 2. Write a program where Animal → Mammal → Dog and each class has
# #  its own method. Call all
# # methods using the Dog class.
# class Animal:
#     def display(self,colour):
#         self.colour=colour
#         print('this is animal',self.colour)
# class Mamal(Animal):
#     def deis(self,stan_size,colour):
#         super().display(colour)
#         self.stan=stan_size
#         print('stan k size hai',self.stan)
# class Dog(Mamal):
#     def deie(self,breed,stan_size,colour):
#         super().deis(colour,stan_size)
#         self.breed=breed
#         print('the breed is',self.breed)
# obj=Dog()
# obj.deie('labra',8,'white')
    
# # 3. Create a class Vehicle, then Car inherits from it, and 
# # SportsCar inherits from Car. Add methods
# # at each level.
# class Vehicle:
#     def pro(self,type):
#         self.type=type
#         print('this vehicle',{self.type})
# class Car(Vehicle):
#     def p(self,brand,type):
#         self.brand=brand
#         super().pro(type)
#         print('the car brand is',self.brand)
# class Supercar(Car):
#     def c(self,brand,cc,type):
#         super().p(brand,type)
#         self.cc=cc
#         print('the car cc is ',self.cc)
# obj=Supercar()
# obj.c('farrari',4500,'car')

# # 4. Demonstrate constructor chaining in multilevel 
# # inheritance using super().
# class Cons:
#     def __init__(self,name):
#         self.name=name
#         print('this is cons',self.name)
# class prod(Cons):
#     def __init__(self, name):
#         super().__init__(name)
#         print('this is prod')
# obj=prod('jatin')

# # 5. Create a class Shape → Rectangle → Square and calculate area at each level.
# class Shape:
#     def shape(self):
#         print('area is ariyng')
# class Reactangle(Shape):
#     def arr(self,br,l):
#         self.br=br
#         self.l=l
#         print('the area of reactangle is ',br*l)
# class Sqare(Reactangle):
#     def arry(self,len,br,l):
#         self.len=len
#         super().arr(br,l)
#         print(len*len)
# obj=Sqare()
# obj.arry(10,15,16)
# # 6. Write a program showing method overriding in multilevel
# #  inheritance.
# class A:
#     def s(self):
#         print('this is process')
# class B(A):
#     def default(self,work):
#         self.work=work
#         print('this is th wordk',self.work)
# class C(B):
#     def vevualt(self,work,work1):
#         self.work1=work1
#         super().default(work)
#         print('this is work 2',self.work1)
# obj=C()
# obj.vevualt('enf','gnh')
# # 7. Create a class Student → GraduateStudent → PhDStudent and 
# # add attributes progressively.
# class Student:
#     def pr(self,name):
#         self.name=name
#         print('the access',self.name)
# class Graduatestudent(Student):
#     def gr(self,name,age):
#         self.age=age
#         super().pr(name)
#         print('the age is ',self.age)
# class Phd(Graduatestudent):
#     def hr(self,name,age,prof):
#         self.prof=prof
#         super().gr(name,age)
#         print('the dep is ',self.prof)
# obj=Phd()
# obj.hr('jatin',21,'prof')

# # 8. Implement a banking system: Account → SavingsAccount →
# #  FixedDepositAccount.
# class Bs:
#     def pr(self,name):
#         self.name=name
#         print('the access',self.name)
# class Acc(Bs):
#     def gr(self,name,type):
#         self.type=type
#         super().pr(name)
#         print('the  type is ',self.type)
# class Fd(Acc):
#     def hr(self,name,type,int):
#         self.int=int
#         super().gr(name,type)
#         print('the int is ',self.int)
# obj=Fd()
# obj.hr('sbi','saving','13%')
# # 9. Create a class Device → Computer → Laptop and show 
# # functionality extension.
# class Device:
#     def pr(self,name):
#         self.name=name
#         print('the access',self.name)
# class Com(Device):
#     def gr(self,name,type):
#         self.type=type
#         super().pr(name)
#         print('the type is ',self.type)
# class Laptop(Com):
#     def hr(self,name,type,feature):
#         self.feat=feature
#         super().gr(name,type)
#         print('the dep is ',self.feat)
# obj=Laptop()
# obj.hr('windows','linux','screen touch')
# # 10. Write a program where each class in multilevel inheritance 
# # modifies a variable and shows how
# # values change.
# class Program1:
#     def __init__(self,prop):
#         self.prop=prop
#         print(self.prop)
# class B(Program1):
#     def __init__(self, prop,prop2):
#         super().__init__(prop)
#         self.prop2=prop2
#         self.prop+=self.prop2
#         print(self.prop)
# obj=B(45,15)


# MIXED / CONCEPTUAL QUESTIONS
# # 1. Combine both multiple and multilevel inheritance in a single program and demonstrate method
# # calls.
# # Full program
# class Grandparents:
#     def dis(self, gotra):
#         self.gotra = gotra
#         print("Gotra is:", self.gotra)
# class Father(Grandparents):  # Multilevel
#     def dis2(self, gotra, jamen):
#         super().dis(gotra)
#         self.jamen = jamen
#         print("Land is:", self.jamen)
# class Mother:  # Second parent (Multiple inheritance)
#     def dis3(self, property):
#         self.property = property
#         print("Mother's property:", self.property)
# class Child(Father, Mother):  # Multiple + Multilevel
#     def show(self, gotra, jamen, property, own):
#         self.dis2(gotra, jamen)   # from Father → Grandparents
#         self.dis3(property)       # from Mother
#         self.own = own
#         print("Own property:", self.own)
# obj=Child()
# obj.show('Mulani', '5 acres', 'House', 'Car')
# # 2. Create a diamond problem scenario and resolve it using 
# # Python’s MRO.
# # Output first
# class Person:
#     def show(self):
#         print("I am a person")
# class Teacher(Person):
#     def show(self):
#         print("I teach")
# class Student(Person):
#     def show(self):
#         print("I study")
# class TeachingAssistant(Teacher, Student):
#     def show(self):
#         print("I assist teacher")
# obj = TeachingAssistant()
# obj.show()
# print(TeachingAssistant.__mro__)
# # 3. Write a program to print the MRO of a complex
# #  inheritance structure.
# class A:
#     def show(self):
#         print("A")
# class B(A):
#     def show(self):
#         print("B")
#         super().show()
# class C(A):
#     def show(self):
#         print("C")
#         super().show()
# class D(B, C):
#     def show(self):
#         print("D")
#         super().show()
# obj = D()
# obj.show()
# 4. Create a system where one class inherits from two classes,
#  and one of those classes further
# inherits from another (hybrid inheritance).
# Output first
# class A:
#     def show1(self, name):
#         self.name = name
#         print("Name:", self.name)

# class B(A):  # Multilevel part
#     def show2(self, profession):
#         self.profession = profession
#         print("Profession:", self.profession)

# class C:
#     def show3(self, hobby):
#         self.hobby = hobby
#         print("Hobby:", self.hobby)

# class D(B, C): 
#     def show_all(self, name, profession, hobby):
#         self.show1(name)        
#         self.show2(profession)  
#         self.show3(hobby)   
# obj = D()
# obj.show_all("Rahul", "Engineer", "Cricket")
