# # 1. Vehicle → Car
# # Vehicle: brand, speed. Car: fuel_type. Use super(). Display all.
# class Vechile:
#     def __init__(self,brand,speed):
#         self.brand=brand
#         self.speed=speed
# class Car(Vechile):
#     def __init__(self, brand, speed,fuel_type,):
#         super().__init__(brand, speed)
#         self.fuel=fuel_type
# obj=Car('supra',350,'specific oil')
# print(obj.brand)

# # 2. Person → Teacher
# # Person: name, age. Teacher: subject. Use super(). Display all.
# class Person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
# class Teacher(Person):
#     def __init__(self, name,age,subject):
#         super().__init__(name,age)
#         self.s=subject
# obj=Teacher('anil',45,'maths')
# print(obj.n)
# # 3. Employee → Manager
# # Employee: emp_id, salary. Manager: department. Use super().
# class Employee:
#     def __init__(self,id,salary):
#         self.i=id
#         self.s=salary
# class Manager(Employee):
#     def __init__(self, id,salary,dep):
#         super().__init__(id,salary)
#         self.d=dep
# obj=Manager(13,45000,'hr')
# print(obj.s)
# # 4. Product → Electronics
# # Product: name, price. Electronics: warranty_years. Use super().
# class product:
#     def __init__(self,name,price):
#         self.n=name
#         self.p=price
# class Electronice(product):
#     def __init__(self, name,price,warranty_yr):
#         super().__init__(name,price)
#         self.w=warranty_yr
# obj=Electronice('jatin',45000,5)
# print(obj.p)
# # 5. Animal → Dog
# # Animal: name, species. Dog: breed. Use super().
# class Animal:
#     def __init__(self,name,species):
#         self.n=name
#         self.s=species
# class Dog(Animal):
#     def __init__(self, name,species,bread):
#         super().__init__(name,species)
#         self.b=bread
# obj=Dog('anil','labra','her')
# print(obj.n)
# 6. Account → SavingsAccount
# Account: account_number, balance. SavingsAccount: interest_rate. Use super().
# class Account:
#     def __init__(self,acc,bal):
#         self.a=acc
#         self.b=bal
# class Saving(Account):
#     def __init__(self, acc,bal,int):
#         super().__init__(acc,bal)
#         self.i=int
# obj=Saving(12234,45000,12)
# print(obj.i)
# 7. User → Admin
# User: username, email. Admin: permissions. Use super().
# class User:
#     def __init__(self,name,email):
#         self.n=name
#         self.e=email
# class Admin(User):
#     def __init__(self, name,email,permission):
#         super().__init__(name,email)
#         self.p=permission
# obj=Admin('anil','jatinmulani@gmail.com','maths')
# print(obj.e)
# # 8. Book → Ebook
# # Book: title, author. Ebook: file_size. Use super().
# class Book:
#     def __init__(self,title,author):
#         self.t=title
#         self.a=author
# class Ebook(Book):
#     def __init__(self, title,author,file_size):
#         super().__init__(title,author)
#         self.s=file_size
# obj=Ebook('anil','dev',45)
# print(obj.t)
# # 9. Appliance → WashingMachine
# # Appliance: brand, power. WashingMachine: capacity. Use super().
# class Appliance:
#     def __init__(self,brand,power):
#         self.b=brand
#         self.p=power
# class Washingmachine(Appliance):
#     def __init__(self, brand,power,capacity):
#         super().__init__(brand,power)
#         self.c=capacity
# obj=Washingmachine('MARUTI',45,4500)
# print(obj.b)
# # 10. Shape → Circle
# # Shape: color. Circle: radius. Use super().
# class Shape:
#     def __init__(self,color):
#         self.c=color
# class Circle(Shape):
#     def __init__(self, colour,radius):
#         super().__init__(colour)
#         self.r=radius
# obj=Circle('red',45)
# print(obj.c)
# # 11. Device → Laptop
# # Device: name, price. Laptop: ram. Use super().


# class Device:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class Laptop(Device):
#     def __init__(self, name, price, ram):
#         super().__init__(name, price)
#         self.ram = ram

#     def display(self):
#         print(f"name: {self.name}")
#         print(f"price: {self.price}")
#         print(f"ram: {self.ram}")


# obj = Laptop('Dell Inspiron', 60000, '16GB')
# obj.display()
# # 12. Food → Fruit
# # Food: name, calories. Fruit: vitamin_content. Use super().
# class Food:
#     def __init__(self, name, calories):
#         self.name = name
#         self.calories = calories


# class Fruit(Food):
#     def __init__(self, name, calories, vitamin_content):
#         super().__init__(name, calories)
#         self.vitamin_content = vitamin_content

#     def display(self):
#         print(f"name: {self.name}")
#         print(f"calories: {self.calories}")
#         print(f"vitamin_content: {self.vitamin_content}")


# obj = Fruit('Apple', 95, 'Vitamin C')
# obj.display()


# # 13. Company → Startup
# # Company: name, location. Startup: funding_amount. Use super().
# class Company:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location


# class Startup(Company):
#     def __init__(self, name, location, funding_amount):
#         super().__init__(name, location)
#         self.funding_amount = funding_amount

#     def display(self):
#         print(f"name: {self.name}")
#         print(f"location: {self.location}")
#         print(f"funding_amount: {self.funding_amount}")


# obj = Startup('TechX', 'Bangalore', '5 Crore')
# obj.display()
# # 14. Movie → WebSeries
# # Movie: title, duration. WebSeries: number_of_seasons. Use super().

# class Movie:
#     def __init__(self, title, duration):
#         self.title = title
#         self.duration = duration


# class WebSeries(Movie):
#     def __init__(self, title, duration, number_of_seasons):
#         super().__init__(title, duration)
#         self.number_of_seasons = number_of_seasons

#     def display(self):
#         print(f"title: {self.title}")
#         print(f"duration: {self.duration}")
#         print(f"number_of_seasons: {self.number_of_seasons}")


# obj = WebSeries('Breaking Bad', '50 min per episode', 5)
# obj.display()
# # 15. Bank → Loan
# # Bank: name, branch. Loan: loan_amount. Use super().
# class Bank:
#     def __init__(self, name, branch):
#         self.name = name
#         self.branch = branch


# class Loan(Bank):
#     def __init__(self, name, branch, loan_amount):
#         super().__init__(name, branch)
#         self.loan_amount = loan_amount

#     def display(self):
#         print(f"name: {self.name}")
#         print(f"branch: {self.branch}")
#         print(f"loan_amount: {self.loan_amount}")


# obj = Loan('SBI', 'Delhi', 500000)
# obj.display()
# # 16. Course → OnlineCourse
# # Course: course_name, duration. OnlineCourse: platform. Use super().

# class Course:
#     def __init__(self, course_name, duration):
#         self.course_name = course_name
#         self.duration = duration


# class OnlineCourse(Course):
#     def __init__(self, course_name, duration, platform):
#         super().__init__(course_name, duration)
#         self.platform = platform

#     def display(self):
#         print(f"course_name: {self.course_name}")
#         print(f"duration: {self.duration}")
#         print(f"platform: {self.platform}")


# obj = OnlineCourse('Python Programming', '3 months', 'Coursera')
# obj.display()
# # 17. Game → MobileGame
# # Game: title, genre. MobileGame: size. Use super().

# class Game:
#     def __init__(self, title, genre):
#         self.title = title
#         self.genre = genre


# class MobileGame(Game):
#     def __init__(self, title, genre, size):
#         super().__init__(title, genre)
#         self.size = size

#     def display(self):
#         print(f"title: {self.title}")
#         print(f"genre: {self.genre}")
#         print(f"size: {self.size}")


# obj = MobileGame('BGMI', 'Battle Royale', '1.5GB')
# obj.display()
# # 18. Hospital → Doctor
# # Hospital: name, location. Doctor: specialization. Use super().

# class Hospital:
#     def __init__(self, name, location):
#         self.name = name
#         self.location = location


# class Doctor(Hospital):
#     def __init__(self, name, location, specialization):
#         super().__init__(name, location)
#         self.specialization = specialization

#     def display(self):
#         print(f"name: {self.name}")
#         print(f"location: {self.location}")
#         print(f"specialization: {self.specialization}")


# obj = Doctor('City Hospital', 'Jaipur', 'Cardiologist')
# obj.display()

# class Transport:
#     def __init__(self, mode, fare):
#         self.mode = mode
#         self.fare = fare


# class Bus(Transport):
#     def __init__(self, mode, fare, route_number):
#         super().__init__(mode, fare)
#         self.route_number = route_number

#     def display(self):
#         print(f"mode: {self.mode}")
#         print(f"fare: {self.fare}")
#         print(f"route_number: {self.route_number}")


# obj = Bus('Public', 20, 'RJ14-21')
# obj.display()
# # 20. Clothing → Shirt
# # Clothing: brand, size. Shirt: color. Use super().

# class Clothing:
#     def __init__(self, brand, size):
#         self.brand = brand
#         self.size = size


# class Shirt(Clothing):
#     def __init__(self, brand, size, color):
#         super().__init__(brand, size)
#         self.color = color

#     def display(self):
#         print(f"brand: {self.brand}")
#         print(f"size: {self.size}")
#         print(f"color: {self.color}")


# obj = Shirt('Nike', 'L', 'Black')
# obj.display()
# class CngCar:
#     cng_prop = 'This car will run with cng'

#     def __init__(self, cylinder):
#         self.cylinder = cylinder

#     def display(self):
#         print('This is the CNG car Property!')


# class PetrolCar:
#     petrol_prop = 'This car will run with petrol'

#     def __init__(self, tank):
#         self.tank = tank

#     def display(self):
#         print('This is the petrol car property!')


# class HybridCar(CngCar, PetrolCar):

#     def __init__(self, tank, cylinder):
#         CngCar.__init__(self, cylinder)
#         PetrolCar.__init__(self, tank)


# car = HybridCar(20, 50)

# print(car.tank)
# print(car.cylinder)
# car.display()
