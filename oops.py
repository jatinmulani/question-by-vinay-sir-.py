# # 1. Create a class called Student that has a class attribute school_name and
# # instance attributes name and age which are initialized using a constructor. Create
# # three objects and print both the class attribute and instance attributes for each
# # object.
# class Student:
#     school_name='subodh'
# obj=Student()
# print(obj.school_name)
# # 2. Create a class called Car that has a class attribute wheels set to 4. Use a
# # constructor to initialize instance attributes brand and price. Create two objects and
# # show how both objects share the same class attribute but have different instance
# # attributes.
# class Car:
#     wheels=4
#     def __init__(self,brand,price):
#         self.car_brand=brand
#         self.car_price=price
# car1=Car('toyota',20000)
# car2=Car('suzuki',150000)
# print(car1.car_brand,car1.car_price)
# print(car2.car_brand,car2.car_price)
# # 3. Create a class called Employee that has a class attribute company_name.
# # Initialize instance attributes emp_name and salary using a constructor. Create
# # multiple employee objects and print their details along with the common company
# # name.
# class Employee:
#     company_name='itc'
#     def  __init__(self,emp_name,salary):
#         self.emp_name1=emp_name
#         self.tsalary=salary
# emp1=Employee('al',900000)
# emp2=Employee('ja',45000)
# print(emp1.emp_name1,emp1.tsalary)
# print(emp2.emp_name1,emp2.tsalary)
# # 4. Create a class called Mobile that has a class attribute category set to
# # Electronics. Use a constructor to initialize mobile_name and RAM. Create three
# # objects and print all values to clearly understand class vs instance attributes.
# class Mobile:
#     category='electornics'
#     def __init__(self,mobile_name,ram):
#         self.m_mobile=mobile_name
#         self.rramm=ram
# mobile1=Mobile('samsung',32)
# mobile2=Mobile('nothing',16)
# print(mobile1.m_mobile,mobile1.rramm)
# print(mobile2.m_mobile,mobile2.rramm)

# # 5. Create a class called Book that has a class attribute library_name. Initialize
# # instance attributes title and author using a constructor. Create at least two objects
# # and print their complete information.
# class Book:
#     liberay='gkg'
#     def __init__(self,title,author):
#         self.t_title=title
#         self.authorr=author
# book1=Book('jhalak','aakash')
# book2=Book('saheed','bhagat singh')
# print(book1.t_title,book1.authorr)

# # 6. Create a class called Laptop that has a class attribute warranty_years. Use a
# # constructor to initialize brand and price. Create multiple laptop objects and display
# # how the class attribute remains same for all objects.
# class Laptop:
#     warranty_year=10
#     def __init__(self,brand,price):
#         self.b=brand
#         self.p=price
# laptop1=Laptop('hp',47000)
# laptop2=Laptop('dell',55000)
# print(laptop1.b,laptop1.p)
# # 7. Create a class called Person that has a class attribute country. Initialize instance
# # attributes name and age using a constructor. Create three person objects and print
# # their data.
# class Person:
#     country='india'
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
# person1=Person('jatin',45)
# person2=Person('aakil',65)
# print(person1.a,person1.n)
# # 8. Create a class called Bike that has a class attribute type set to Two Wheeler.
# # Use a constructor to initialize bike_name and mileage. Create objects and print all
# # details.
# class Bike:
#     type='two wheeler'
#     def __init__(self,bike_name,mileage):
#         self.b=bike_name
#         self.m=mileage
# bike1=Bike('tvs',45)
# bike2=Bike('mariyo',44)
# print(bike1.b,bike1.m)
# # 9. Create a class called Movie that has a class attribute industry set to Bollywood.
# # Initialize instance attributes movie_name and rating using a constructor. Create
# # multiple movie objects and print the details.
# class Movie:
#     industry='bollywood'
#     def __init__(self,name,rating):
#         self.movie=name
#         self.rate=rating
# movie1=Movie('dhurandhar',10)
# print(movie1.movie,movie1.rate)
# # 10. Create a class called BankAccount that has a class attribute bank_name. Use
# # a constructor to initialize account_holder and balance. Create two account objects
# # and print their information showing both class and instance attributes.
# class Bankaccount:
#     bank_name='sbi'
#     def __init__(self,account_holder,balance):
#         self.name=account_holder
#         self.bal=balance
# bank1=Bankaccount('jatin',45)
# print(bank1.name,bank1.bal)