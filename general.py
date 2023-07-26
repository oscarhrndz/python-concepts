
# 1. Introduction

#  =================================================================

# 2. Variables

# first_name = "Illo"
# last_name = "wan"
# full_name = first_name + " " + last_name
# print("Hello " + full_name)
# print(type(full_name))

# age = 21
# age += 1
# print("Your age is: " + str(age))
# print(type(age))

# height = 250.5
# print("Your height is: " + str(height) + "cm")
# print(type(height))

# human = True
# print("Are you a human: " + str(human))
# print(type(human))

# ============================================================================

# 3. Multiple Assignment

# name = "Illo"
# age = 21
# attractive = True

# name, age, attractive = "Illo", 21, True

# print(name)
# print(age)
# print(attractive)

# ------------------------------------------------------------------------

# 4. String Methods

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# Spongebob = Patrick = Sandy = Squidward = 30


# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)

# =======================================================================

# 5. Type Casting

# Type casting = convert the data type of a value to another data type

# name = "Illo"

# print(len(name))
# print(name.find("o"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("o"))
# print(name.replace("o", "a"))
# print(name*3)

# ===========================================================================

# 6. User Input

# x = 1
# y = 2.0
# z = "3"

# x = str(x)
# y = str(y)
# z = str(z)

# print(x)
# print(y)
# print(z*3)

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# height = float(input("How tall are you?: "))

# print("Hi " + name)
# print("You are " + str(age) + years old")
# print("You are " + str(height) + "cm tall")

# ===========================================================

# 7. Math Functions

# import math
# from os import cpu_count

# pi = 3.14
# x = 1
# y = 2
# z = 3

# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))  || Negative numbers to Positive numbers
# print(pow(pi, 2))
# print(math.sqrt(pi))
# print(max(x, y, z))
# print(min(z, y, z)

# ================================================================

# 8. String Slicing

# Slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

# name = "Illowan"

# first_name = name[4]
# first_name = name[0:4] || name[:4]
# last_name = name[4:7] || name[4:]
# funky_name = name[0:7:3]
# reversed_name = name[::-1]
#
# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# -------------------------

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
#
# slice = slice(7, -4)
#
# print(website1[slice])
# print(website2[slice])

# ====================================================================

# 9. if statement = a block of code that will execute if it's condition is true

# age = int(input("How old are you?: "))
#
# if age >= 18:
#     print("You are an adult")
# elif age == 100:
#     print("You are a century old")
# elif age < 0:
#     print("You haven't been born yet")
# else:
#     print("You are a child")

# =====================================================================

# 10. logical operators (and, or, not) = used to check if two or more conditional statements is true

# temp = int(input("What is the temperature outside?: "))
#
# if temp > 0 and temp <= 30:
#     print("The temperature is good today")
#     print("Go outside")
# elif not(temp > 0 and temp <= 30):
#     print("The temperature is bad today")
#     print("Stay inside")

# =======================================================================

# 11. while loop = a statement that will execute it's block of code,
#                   as long as it's condition remains true

# name = None
#
# while not name:
#     name = input("Enter your name: ")
#
# print("Hello " + name)

# ==============================================================================

# 12. for loop = a statement that will execute it's block of code
#                a limited amount of times
#
#                while loop = unlimited
#                for loop = limited
# import shutil


# import time
# from traceback import print_tb

# for i in range(10):
#     print(i+1)

# for i in range(50, 100+1, 2):
#     print(i)

# for i in "Illo wan":
#     print(i)

# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year")

# ========================================================================

# 13. nested loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iterarion of the "outer loop"

# rows = int(input("How many rows?: "))
# columns = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
#
# for i in range(rows):
#     for j in range(columns):
#         print(symbol) || print(symbol, end="")
#     print()

# ========================================================================

# 14. Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phone_number = "123-456-7890"
#
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1, 21):
#
#     if i == 13:
#         pass
#     else:
#         print(i)

# =========================================================================

# 15. list = used to store multiple items in a single variable

# food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]

# food[0] = "sushi"
# food.append("ice cream")
# food.remove("hotdog")
# food.pop()
# food.insert(0, "cake")
# food.sort()
# food.clear()

# print(food[1])

# for x in food:
#     print(x)

# =========================================================================

# 16. 2D lists = a list of lists

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
#
# food = [drinks, dinner, dessert]
#
# print(food) || (food[1]) || (food[0][2])

# ==========================================================================

# 17. tuple =       collection which is ordered and unchangeable
#                   used to group together related data

# student = ("Illo", 21, "male")
#
# print(student.count("Illo"))
# print(student.index("male"))
#
# for x in student:
#     print(x)
#
# if "Illo" in student:
#     print("Illo ta aqui")

# ==========================================================================

# 18. set = collection which is unordered, unindexed. No duplicate values

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes)
# dinner_table = utensils.union(dishes)
#
# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))
#
# for x in utensils:
#     print(x)

# ====================================================================

# 19. dictionary =      A changeable, unordered collection of unique key: value pairs
#                       Fast because they use hashing, aloow us to access a value quickly

# capitals = {'USA': 'Washington DC',
#             'India': 'New Dehli',
#             'China': 'Beijing',
#             'Russia': 'Moscow'}
#
# capitals.update({'Germany': 'Berlin'})
# capitals.update({'USA': 'Las Vegas'})
# capitals.pop('China')
# capitals.clear()
#
# print(capitals['Russia'])
# print(capitals.get('Germany'))
# print(capitals.key())
# print(capitals.values())
# print(capitals.items())
#
# for key, value in capitals.items():
#     print(key, value)

# =============================================================================

# 20. index operator [] = gives access to a sequence's element (str, list, tuples)

# name = "Illo Wan!"
#
# if(name[0].islower()):
#     name = name.capitalize()
#
# first_name = name[:4].upper()
# last_name = name[5:].lower()
# last_character = name[-1]
#
# print(first_name)
# print(last_name)
# print(last_character)

# ==============================================================================

# 21. function =    a block of code which is executed only when it is called

# def hello(first_name, last_name, age):
#     print("Hello " + first_name + " " + last_name)
#     print("You are " + str(age) + " years old")
#     print("Have a nice day")
#
# hello("Illo", "Wan", 21)

# ==============================================================================

# 22. return statement =    Functions send Python values/objects back to the caller.
#                           These values/objects are known as the function's return value

# def multiply(number1, number2):
#     return number1 * number2
#
# x = multiply(6, 8)
#
# print(x)

# ================================================================================

# 23. keyword arguments =   arguments preceded by an identifier when we pass them to a function
#                           The order of the arguments doesn't matter, unlike positional arguments
#                           Python knows the names of the arguments that our function receives

# def hello(first, middle, last):
#     print("Hello " + first + " " + middle + " " + last)
#
# hello(last="Illo", middle="Wan", first="Bokeron")

# ============================================================================

# 24. nested functions calls =  function calls inside other function calls
#                               innermost function calls are resolved first
#                               returned value is used as argument for the next outer function

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num=round(num)
# print(num)

# print(round(abs(float(input("Enter a whole positive number: ")))))

# ====================================================================================

# 25. scope =   The region that a variable is recognized.
#               A variable is only available from inside the region it is created.
#               A global and locally scoped versions of a variable can be created

# name = "Illo"   # global scope (available inside & outside functions)
#
# def display_name():
#     name = "Wan"   # local scope (available only inside this function
#     print(name)
#
# display_name()
# print(name)

# =====================================================================================

# 26. *args =   parameter that will pack all arguments into a tuple
#               useful so that a function can accept a varying amount of arguments

# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#     return sum
#
# print(add(1,2,3))

# ======================================================================================

# 27. **kwargs =    parameter that will pack all arguments into a dictionary
#                   useful so that a function can accept a varying amount of keyword argument

# def hello(**kwargs):
#     # print("Hello " + kwargs['first'] + " " + last)
#     print("Hello", end=" ")
#     for key, value in kwargs.items():
#         print(value, end=" ")
#
# hello(first = "bro", middle = "dude", last = "code")

# ======================================================================================

# 28. str.format() =    optional method that gives users
#                       more control when displaying output

# animal = "cow"
# item = "moon"
#
# print("The " + animal + " jumped over the " + item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item)) # positional argument
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) # keyword argument
#
# text = "The {} jumped over the {}"
# print(text.format(animal, item))

# name = "Illo"
#
# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))

# number = 1000
#
# print("The number pi is {:.3f}".format(number))
# print("The number pi is {:,}".format(number))
# print("The number pi is {:b}".format(number))
# print("The number pi is {:o}".format(number))
# print("The number pi is {:x}".format(number))
# print("The number pi is {:e}".format(number))

# ====================================================================================

# 29. random numbers

# import random
#
# x = random.randint(1, 6)
# y = random.random()
#
# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)
#
# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
#
# random.shuffle(cards)
#
# print(cards)

# 30. exception =   events detected during execution that interrupt the flow of a program

# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
#     print(result)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# except ValueError as e:
#     print("Enter only members pls")
# except Exception as e:
#     print(e)
#     print("something went wrong :(")
# else:
#     print(result)
# finally:
#     print("This will always  execute")

# =================================================================================

# 32. file detection

# import os
#
# path = "M:\\TXT"
#
# if os.path.exists(path):
#     print("That location exists")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory")
# else:
#     print("That location doesn't exist")

# ===========================================================================

# 32. read a file

# try:
#     with open('illo.txt') as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found")
#
# print(file.closed)

# ===============================================================================

# 33. write a file

# text = "Yoooooooooo\nThis is some text\nHave a good day\n"
#
# with open('illo.txt', 'w') as file:
#     file.write(text)

# =================================================================================

# 34. copy a file

#       copyfile() =    copies contents of a file
#       copy() =        copyfile() + permission mode + destination can be a directory
#       copy2() =       copy() + copies metadata (file's creation and modification times)

# import shutil
#
# shutil.copy2('illo.txt', 'C:\\Users\\El Macaquiño\\PycharmProjects\\helloWorld\\venv\\copy.txt') #src, dst

# ===================================================================================

# 35. move a file

# import os
#
# source = "test.txt"
# destination = "C:\\Users\\El Macaquiño\\PycharmProjects\\helloWorld\\venv\\test.txt"
#
# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source + " was moved")
# except FileNotFoundError:
#     print(source + " was not found")

# ===============================================================================

# 36. delete a file
#
#       os.remove(path)         # delete a file
#       os.rmdir(path)          # delete an empty directory
#       shutil.rmtree(path)     # delete a directory containing files

# import os
# import shutil
#
# path = "C:\\Users\\El Macaquiño\\PycharmProjects\\helloWorld\\venv\\copy.txt"
#
# try:
#     os.remove(path)
#     os.rmdir(path)
#     shutil.rmtree(path)
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to delete that")
# except(OSError):
#     print("You cannot delete that using that function")
# else:
#     print(path + " was deleted")

# ===================================================================================

# 37. modules

# help("modules")

#       modules = a file containing python code. May functions, classes, etc.
#       used with modular programming, which is to separate a program into parts

# import messages as msg
#
# msg.hello()
# msg.bye()

# from messages import *
#
# hello()
# bye()

# =============================================================================

# 38. rock, paper, scissors game

# import random
#
# points_player = 0
# points_computer = 0
#
# while True:
#     choices = ["rock", "paper", "scissors"]
#
#     computer = random.choice(choices)
#     player = None
#
#     while player not in choices:
#         player = input("rock, paper or scissors?: ").lower()
#
#     if player == computer:
#         print("computer: ", computer)
#         print("player: ", player)
#         print("Tie")
#     elif player == "rock":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose")
#             points_computer += 1
#             print("Player {} - {} Computer".format(points_player, points_computer))
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win")
#             points_player += 1
#             print("Player {} - {} Computer".format(points_player, points_computer))
#
#     elif player == "paper":
#         if computer == "scissors":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose")
#             points_computer += 1
#             print("Player {} - {} Computer".format(points_player, points_computer))
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win")
#             points_player += 1
#             print("Player {} - {} Computer".format(points_player, points_computer))
#
#     elif player == "scissors":
#         if computer == "paper":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You win")
#             points_player += 1
#             print("Player {} - {} Computer".format(points_player, points_computer))
#         if computer == "rock":
#             print("computer: ", computer)
#             print("player: ", player)
#             print("You lose")
#             points_computer += 1
#             print("Player {} - {} Computer".format(points_player, points_computer))
#
#     play_again = input("Play again? (YES[Y]/NO[N]: ").upper()
#
#     if play_again != "Y":
#         break
#
# print("Bye, GG")

# 39. quiz game


# def new_game():
#
#     guesses = []
#     correct_guesses = 0
#     question_num = 1
#
#     for key in questions:
#         print("----------------------")
#         print(key)
#         for i in options[question_num-1]:
#             print(i)
#         guess = input("Enter (A, B, C or D): ")
#         guess = guess.upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key),guess)
#         question_num += 1
#
#     display_score(correct_guesses, guesses)
#
#
# def check_answer(answer, guess):
#
#     if answer == guess:
#         print("CORRECT")
#         return 1
#     else:
#         print("Wrong")
#         return 0
#
#
# def display_score(correct_guesses, guesses):
#     print("--------------------------")
#     print("RESULTS")
#     print("--------------------------")
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end=" ")
#     print()
#
#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end=" ")
#     print()
#
#     score = int((correct_guesses/len(questions))*100)
#     print("Your score is: " + str(score) + "%")
#
#
# def play_again():
#
#     response = input("Do you want to play again? (Yes[Y] or No[N]: ")
#     response = response.upper()
#
#     if response == "Y":
#         return True
#     else:
#         return False
#
#
# questions = {
#     "Who created Pyhton? ": "A",
#     "What year was Python created?: ": "B",
#     "Pyhton is tributed to which comedy group?: ": "C",
#     "Is the Earth round?: ": "A"
# }
#
# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
#            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#            ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"]]
#
# new_game()
#
# while play_again():
#     new_game()
#
# print("Bye")

# ===============================================================================

# 40. Object Oriented Programming (OOP)

# from car import Car
#
# car_1 = Car("Chevy", "Corvette", 2021, "blue")
# car_2 = Car("Ford", "Mustang", 2022, "red")
#
# car_2.drive()
# car_2.stop()

# ==========================================================================

# 41. class variables

# from car import Car
#
# car_1 = Car("Chevy", "Corvete", 2021, "blue")
# car_2 = Car("Ford", "Mustang", 2022, "red")

# car_1.wheels = 2
#
# print(car_1.wheels)
# print(car_2.wheels)

# Car.wheels = 2
#
# print(car_1.wheels)
# print(car_2.wheels)

# ==========================================================================

# 42. inheritance

# class Animal:
#
#     alive = True
#
#     def eat(self):
#         print("This animal is eating")
#
#     def slumber(self):
#         print("This animal is sleeping")
#
#
# class Rabbit(Animal):
#     def run(self):
#         print("This rabbit is running")
#
#
# class Fish(Animal):
#     def swim(self):
#         print("This fish is swimming")
#
#
# class Hawk(Animal):
#     def fly(self):
#         print("This hawk is flying")
#
#
# rabbit = Rabbit()
# fish = Fish()
# hawk = Hawk()
#
# # print(rabbit.alive)
# # fish.eat()
# # hawk.sleep()
#
# rabbit.run()
# fish.swim()
# hawk.fly()

# ============================================================================

# 43. multilevel inheritance = when a derived (child) class inherits another derived (child) class

# class Organism:
#
#     alive = True
#
#
# class Animal(Organism):
#
#     def eat(self):
#         print("This animal is eating")
#
#
# class Dog(Animal):
#
#     def bark(self):
#         print("This dog is barking")
#
# dog = Dog()
# print(dog.alive)
# dog.eat()
# dog.bark()

# ==============================================================================

# 44. multiple inheritance = when a child class is derived from more than one parent class

# class Prey:
#
#     def flee(self):
#         print("This animal flees")
#
#
# class Predator:
#
#     def hunt(self):
#         print("This animal is hunting")
#
#
# class Rabbit(Prey):
#     pass
#
#
# class Hawk(Predator):
#     pass
#
#
# class Fish(Prey, Predator):
#     pass
#
#
# rabbit = Rabbit()
# hawk = Hawk()
# fish = Fish()
#
# rabbit.flee()
# hawk.hunt()
# fish.flee()
# fish.hunt()

# ===========================================================================

# 45. method overriding

# class Animal:
#
#     def eat(self):
#         print("This animal is eating")
#
#
# class Rabbit(Animal):
#
#     def eat(self):
#         print("This rabbit is eating a carrot")
#
#
# rabbit = Rabbit()
# rabbit.eat()

# =============================================================================

# 46. method chaining = calling multiple methods sequentially
#                       each call performs an action on the same object and returns self

# class Car:
#
#     def turn_on(self):
#         print("You start the engine")
#         return self
#
#     def drive(self):
#         print("You drive the car")
#         return self
#
#     def brake(self):
#         print("You step on the brakes")
#         return self
#
#     def turn_off(self):
#         print("You turn off the engine")
#         return self
#
#
# car = Car()
#
# car.turn_on().drive()
#
# car.brake().turn_off()

# car.turn_on().drive().brake().turn_off()
# car.turn_on()\
#     .drive()\
#     .brake()\
#     .turn_off()

# ===============================================================================

# 47. super() = function used to give access to the methods of a parent class.
#               Returns a temporary object of a parent class when used

# class Rectangle:
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#
# class Square(Rectangle):
#
#     def __init__(self, length, width):
#         super().__init__(length, width)
#
#     def area(self):
#         return self.length*self.width
#
#
# class Cube(Rectangle):
#
#     def __init__(self, length, width, height):
#         super().__init__(length, width)
#         self.height = height
#
#     def volume(self):
#         return self.length*self.width*self.height
#
#
# square = Square(3, 3)
# cube = Cube(3, 3, 3)
#
# print(square.area())
# print(cube.volume())

# =========================================================================

# 48. abstract classes

# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation

# from abc import ABC, abstractmethod
#
#
# class Vehicle(ABC):
#
#     @abstractmethod
#     def go(self):
#         pass
#
#     @abstractmethod
#     def stop(self):
#         pass
#
#
# class Car(Vehicle):
#
#     def go(self):
#         print("You drive the car")
#
#     def stop(self):
#         print("This car is stopped")
#
#
# class Motorcycle(Vehicle):
#
#     def go(self):
#         print("You ride the motorcycle")
#
#     def stop(self):
#         print("This motorcycle is stopped")
#
#
# car = Car()
# motorcycle = Motorcycle()
#
# car.go()
# motorcycle.go()
#
# car.stop()
# motorcycle.stop()

# ===============================================================================

# 49. objects as arguments

# class Car:
#
#     color = None
#
#
# class Motorcycle:
#
#     color = None
#
#
# def change_color(vehicle, color):
#
#     vehicle.color = color
#
#
# car_1 = Car()
# car_2 = Car()
# car_3 = Car()
#
# bike_1 = Motorcycle()
#
# change_color(car_1, "red")
# change_color(car_2, "white")
# change_color(car_3, "blue")
# change_color(bike_1, "black")
#
# print(car_1.color)
# print(car_2.color)
# print(car_3.color)
# print(bike_1.color)

# ==============================================================================

# 50. Duck typing = concept where the class of an object is less important than the methods/attributes
#                   class type is not checked if minimum methods/attributes are present
#                   "If it walks like a duck, and it quacks like a duck, then it must be a duck"

# class Duck:
#
#     def walk(self):
#         print("This duck is walking")
#
#     def talk(self):
#         print("This duck is quacking")
#
#
# class Chicken:
#
#     def walk(self):
#         print("This chicken is walking")
#
#     def talk(self):
#         print("This chicken is clucking")
#
#
# class Person():
#
#     def catch(self, duck):
#         duck.walk()
#         duck.talk()
#         print("You caught the critter")
#
#
# duck = Duck()
# chicken = Chicken()
# person = Person()
#
# person.catch(duck)

# ========================================================================

# 51. walrus operator :=
#
# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)
#
# print(happy := True)

# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# foods = list()
# while food := input("What food do you like?: ") != "quit":
#     foods.append(food)

# ==================================================================================

# 52. functions to variables

# def hello():
#     print("Hello")

# print(hello)
# hi = hello
# print(hi)

# hi = hello
# hello()
# hi()

# say = print
# say("Illo")

# ==============================================================================================

# 53. Higher Order Function = a function that either:
#                             1. Accepts a function as an argument
#                                or
#                             2. Returns a function
#                             (In Python, functions are also treated as objects)

# def loud(text):
#     return text.upper()
#
#
# def quiet(text):
#     return text.lower()
#
#
# def hello(func):
#     text = func("Hello")
#     print(text)
#
#
# hello(loud)
# hello(quiet)

# def divisor(x):
#     def dividend(y):
#         return y / x
#     return dividend
#
#
# divide = divisor(2)
# print(divide(10))

# ===============================================================================================

# 54. lambda function = function written in 1 line using lambda keyword
#                       accepts any number of arguments, but only has one expression
#                       (think of it as a shortcut)
#                       (useful if needed for a short period of time, throw-away)
#
# lambda parameters: expression

# def double(x):
#     return x * 2
#
# print(double(5))

# double = lambda x: x * 2
# multiply = lambda x, y: x * y
# add = lambda x, y, z: x + y + z
# full_name = lambda first_name, last_name: first_name + " " + last_name
# age_check = lambda age: True if age >= 18 else False
# print(age_check)

# ======================================================================================

# 55. sort() method     = used with lists
#     sort() function   = used with iterables


# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]
#
# students.sort(reverse=True)
#
# for i in students:
#     print(i)

# students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs")
#
# sorted_students = sorted(students, reverse=True)
#
# for i in students:
#     print(i)

# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick", "D", 36),
#             ("Spongebob", "B", 20),
#             ("Mr. Krabs", "C", 78)]
#
# age = lambda ages:ages[2]
# # students.sort(key=age, reverse=True)
# sorted_students = sorted(students, key=age)
#
# for i in students:
#     print(i)

# =======================================================================================

# 56. map() =   applies a function to each item in an iterable (list, tuple, etc.
#
# map(function, iterable)

# store = [("shirt", 20.00),
#          ("pants", 25.00),
#          ("jacket", 50.00),
#          ("socks", 10.00)]
#
# # to_euros = lambda data: (data[0], data[1]*0.82)
# to_dollars = lambda data: (data[0], data[1]/0.82)
#
# # store_euros = list(map(to_euros, store))
# #
# # for i in store_euros:
# #     print(i)
#
# store_dollars = list(map(to_dollars, store))
#
# for i in store_dollars:
#     print(i)

# ========================================================================================

# 57. filter() = creates a collection of elements from an iterable for which a function returns true
#
# filter(function, iterable)

# friends = [("Rachel", 19),
#            ("Monica", 18),
#            ("Phoebe", 17),
#            ("Joey", 16),
#            ("Chandler", 21),
#            ("Ross", 20)]
#
# age = lambda data:data[1] >= 18
#
# drinking_buddies = list(filter(age, friends))
#
# for i in drinking_buddies:
#     print(i)

# =================================================================================================

# 58. reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#                performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

# import functools
#
# letters = ["H", "E", "L", "L", "O"]
# word = functools.reduce(lambda x, y, :x + y, letters)
# print(word)
#
# factorial = [5, 4, 3, 2, 1]
# result = functools.reduce(lambda x, y, :x * y, factorial)
# print(result)

# =============================================================================================

# 59. list comprehension = a way to create a new list with less syntax
#                          can mimic certain lambda functions, easier to read
#                          list = [expression for item in iterable]
#                          list = [expression for item in iterable if conditional]
#                          list = [expression (if/else) for item in iterable]

# squares = []                    # create an empty list
# for i in range(1, 11):          # create a for loop
#     squares.append(i * i)       # define what each loop iteration should do
# print(squares)
#
# squares = [i * i for i in range(1, 11)]
# print(squares)

# students = [100, 90, 80, 70, 60, 50, 40, 30, 0]
#
# # passed_students = list(filter(lambda x: x >= 60, students))
#
# # passed_students = [i for i in students if i >= 60]
#
# passed_students = [i if i >= 60 else "FAILED" for i in students]
#
# print(passed_students)

# ========================================================================================

# 60. dictionary comprehension = create dictionaries using an expression
#                                can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key, value) in iterable}
# dictionary = {key: expression for (key, value) in iterable if conditional}
# dictionary = {key: (if/else) for (key, value) in iterable}
# dictionary = {key: function(value) for (key, value) in iterable}

# cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
#
# cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
# print(cities_in_C)

# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities.items()}
# print(desc_cities)

# def check_temp(value):
#     if value >= 70:
#         return "HOT"
#     elif 69 >= value >= 40:
#         return "WARM"
#     else:
#         return "COLD"
#
# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key, value) in cities.items()}
# print(desc_cities)

# ===========================================================================================

# 61. zip(*iterables) = aggregate elements from two or more iterables (list, tuples, set, etc.)
#                       creates a zip object with paired elements stored in tuples for each element

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")
#
# users = dict(zip(usernames, passwords))
#
# print(type(users))
#
# for key, value in users.items():
#     print(key + " : " + value)

# usernames = ["Dude", "Bro", "Mister"]
# passwords = ("p@ssword", "abc123", "guest")
# login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]
#
# users = zip(usernames, passwords, login_date)
#
# for i in users:
#     print(i)

# ============================================================================================

# 62. if __name__ == '__main__'

# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variables", one of which is ___name__
# Python will assign the __name__ variable a value of '__main__' if it's
# the initial module being run

# if __name__ == '__main__':
#     print("running this module directly")
# else:
#     print("running other module indirectly")

# ==========================================================================================

# 63. time module

# import time

# print(time.ctime(10000))    # convert a time expressed in seconds since epoch to a readable string
# #                             epoch = when your computer thinks time began (reference time)
#
# print(time.time())      # return current seconds since epoch

# print(time.ctime(time.time()))

# time_object = time.localtime()
# time_object = time.gmtime()
# # print(time_object)
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# time_string = "20 April, 2020"
# time_object = time.strptime(time_string, "%d %B, %Y")
# print(time_object)

# # (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# # (year, month, day, hours, minutes, secs, #day of the week, #day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)

# ===========================================================================================

# 64. threading

# thread =  a flow of execution. Like a separate order of instructions.
#           However each thread takes a turn running to achieve concurrency
#           GIL = (global interpreter lock),
#           allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal eventes (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

# import threading
# import time
#
#
# def eat_breakfast():
#     time.sleep(3)
#     print("You eat breakfast")
#
#
# def drink_coffee():
#     time.sleep(4)
#     print("You drank coffe")
#
#
# def study():
#     time.sleep(5)
#     print("You finish studying")
#
# x = threading.Thread(target=eat_breakfast, args=())
# x.start()
#
# y = threading.Thread(target=eat_breakfast, args=())
# y.start()
#
# z = threading.Thread(target=eat_breakfast, args=())
# z.start()
#
# x.join()
# y.join()
# z.join()
#
# # eat_breakfast()
# # drink_coffee()
# # study()
#
# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())

# ==============================================================================================

# 65. daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

# import threading
# import time

# def timer():
#     print()
#     count = 0
#     while True:
#         time.sleep(1)
#         count += 1
#         print("logged in for: ", count, "seconds")

# x = threading.Thread(target=timer, daemon = True)
# x.start()

# # x.setDaemon(True)
# # print(x.isDaemon)

# answer = input("Do you wish to exit?")

# =============================================================================

# 66. multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                       multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                       multithreading = better for io bound tasks (waiting around)

# from multiprocessing import Process, cpu_count
# import time
#
#
# def counter(num):
#     count = 0
#     while count < num:
#         count += 1
#
#
# def main():
#
#     # print(cpu_count())
#
#     a = Process(target=counter, args=(125000000,))
#     b = Process(target=counter, args=(125000000,))
#     c = Process(target=counter, args=(125000000,))
#     d = Process(target=counter, args=(125000000,))
#     e = Process(target=counter, args=(125000000,))
#     f = Process(target=counter, args=(125000000,))
#     g = Process(target=counter, args=(125000000,))
#     h = Process(target=counter, args=(125000000,))
#
#     a.start()
#     b.start()
#     c.start()
#     d.start()
#     e.start()
#     f.start()
#     g.start()
#     h.start()
#
#     a.join()
#     b.join()
#     c.join()
#     d.join()
#     e.join()
#     f.join()
#     g.join()
#     h.join()
#
#     print("finished in:", time.perf_counter(), "seconds")
#
# if __name__ == '__main__':
#     main()

# ==============================================================================================

# 67. GUI windows

# # widgets = GUI elements: buttons, textboxes, labels, images
# # windows = serves as a container to hold or contain these widgets

# from tkinter import *
#
# window = Tk()   # instantiate an instance of a windows
# window.geometry("420x420")
# window.title("Illo Wan first GUI program")
#
# icon = PhotoImage(file='venv/logo.png')
# window.iconphoto(True, icon)
# window.config(background="#5cfcff")
#
# window.mainloop()   # place window on computer screen, listen for events

# ================================================================================

# 68. label = an area widget that holds text and/or an image within a window

# from tkinter import *
#
# window = Tk()
#
# photo = PhotoImage(file='venv/logo.png')
#
# label = Label(window,
#               text="Hello World",
#               font=('Arial', 40, 'bold'),
#               fg='#00FF00',
#               bg='black',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20,
#               image=photo,
#               compound='top')
# label.pack()
# # label.place(x=100, y=100)
#
# window.mainloop()

# ==========================================================================================

# 69. button = you click it, then it does stuff

# from tkinter import *
#
# count = 0
#
#
# def click():
#     global count
#     count += 1
#     print(count)
#
#
# window = Tk()
#
# photo = PhotoImage(file='venv/like1.png')
#
# button = Button(window,
#                 text="click me!",
#                 command=click,
#                 font=("Comic Sans", 30),
#                 fg="#00FF00",
#                 bg="black",
#                 activeforeground="#00FF00",
#                 activebackground="black",
#                 state=ACTIVE,
#                 image=photo,
#                 compound="bottom")
# button.pack()
#
# window.mainloop()

# =============================================================================================

# 70. entrybox

# entry widget = textbox that accepts a single line of user input

# from tkinter import *
#
#
# def submit():
#     username = entry.get()
#     print("Hello " + username)
#     # entry.config(state=DISABLED)
#
#
# def delete():
#     entry.delete(0, END)
#
#
# def backspace():
#     entry.delete(len(entry.get())-1, END)
#
#
# window = Tk()
#
# entry = Entry(window,
#               font=("Arial", 50),
#               fg="#00FF00",
#               bg="black")
# # entry.insert(0, 'Spongebob')
# # entry.config(show="*")
# # entry.config(state=DISABLED)
#
# entry.pack(side=LEFT)
#
# submit_button = Button(window, text="submit", command=submit)
# submit_button.pack(side=RIGHT)
#
# delete_button = Button(window, text="delete", command=delete)
# delete_button.pack(side=RIGHT)
#
# backspace_button = Button(window, text="backspace", command=backspace)
# backspace_button.pack(side=RIGHT)
#
# window.mainloop()

# ==============================================================================================

# 71. checkbox

# from tkinter import *
#
#
# def display():
#     if(x.get()==1):     # || x.get() || x.get()=="YES"
#         print("You agree")
#     else:
#         print("You don't agree")
#
#
# window = Tk()
#
# x = IntVar()        # || x = BooleanVar() || x = StringVar()
#
# photo = PhotoImage(file='venv/logo.png')
#
# check_button = Checkbutton(window,
#                            text="I agree to something",
#                            variable=x,
#                            onvalue=1,       # || onvalue=True || onvalue="YES"
#                            offvalue=0,      # || offvalue=False || onvalue="NO"
#                            command=display,
#                            font=('Arial',20),
#                            fg='#00FF00',
#                            bg='black',
#                            activeforeground='#00FF00',
#                            activebackground='black',
#                            padx=25,
#                            pady=10,
#                            image=photo,
#                            compound='left')
# check_button.pack()
# window.mainloop()

# ===================================================================================

# 72. radio button = similar to checkbox, but you can only select one from a group

# from tkinter import *
#
# food = ["pizza", "hamburger", "hotdog"]
#
# def order():
#     if(x.get()==0):
#         print("You ordered pizza")
#     elif(x.get()==1):
#         print("You ordered a hamburger")
#     elif(x.get()==2):
#         print("You ordered a hot dog")
#     else:
#         print("huh?")
#
# window = Tk()
#
# pizzaImage = PhotoImage(file='venv/pizza.png')
# hamburgerImage = PhotoImage(file='venv/burger.png')
# hotdogImage = PhotoImage(file='venv/hot_dog.png')
# foodImages = [pizzaImage, hamburgerImage, hotdogImage]
#
# x = IntVar
#
# for index in range(len(food)):
#     radiobutton = Radiobutton(window,
#                               text=food[index],     # adds text to radio buttons
#                               variable=x,           # groups radiobuttons together if they share the same variable
#                               value=index,          # assigns each radiobutton a different value
#                               padx=25,
#                               font=("Impact", 50),
#                               image=foodImages[index],    # adds image to radiobutton
#                               compound='left',            # adds image & text (left-side)
#                               indicatoron=0,              # eliminate circle indicator
#                               width=375,                  # sets width of radio buttons
#                               command=order              # set command of radiobutton to function
#                               )
#     radiobutton.pack(anchor=W)
# window.mainloop()

# =======================================================================================================

# 73. scale

# from tkinter import *
#
# def submit():
#     print("The temperature is: " + scale.get() + "C°")
#
# window = Tk()
#
# hotImage = PhotoImage(file='venv/hot2.png')
# hotLabel = Label(image=hotImage)
# hotLabel.pack()
#
# scale = Scale(window,
#               from_=100,
#               to=0,
#               length=600,
#               orient=VERTICAL,          # orientation if scale
#               font=('Consolas', 20),
#               tickinterval=10,          # adds numeric indicators for value
# #             showvalue=0,              # hide current value
#               resolution=5,             # increment of slider
#               troughcolor='#69EAFF',
#               fg='#FF1C00',
#               bg='#111111'
#               )
# scale.set(((scale['from']-scale['to'])/2)+scale['to'])      # set current value of slider
#
# scale.pack()
#
# coldImage = PhotoImage(file='venv/cold.png')
# coldLabel = Label(image=coldImage)
# coldLabel.pack()
#
# button = Button(window, text='submit', command=submit)
# button.pack()
#
# window.mainloop()

# ====================================================================================================

# 74. listbox = A listing of selectable text items within it is own container

# def submit():

#     food = []

#     for index in listbox.curselection():
#         food.insert(index, listbox.get(index))
        
#     print("You have ordered")


# def add():
#     listbox.insert(listbox.size(), entryBox.get())
#     listbox.config(height=listbox.size())


# def delete():
#     listbox.delete(listbox.curselection())
#     listbox.config(height=listbox.size())


# from tkinter import *

# window = Tk()

# listbox = Listbox(window,
#                   bg="#f7ffde",
#                   font=("Constantia", 35),
#                   width=12)
# listbox.pack()

# listbox.insert(1, 'pizza')
# listbox.insert(2, 'pasta')
# listbox.insert(3, 'garlic bread')
# listbox.insert(4, 'soup')
# listbox.insert(5, 'salad')

# listbox.config(height=listbox.size())

# entryBox = Entry(window)
# entryBox.pack()

# submitButton = Button(window, text="submit", command=submit)
# submitButton.pack()

# addButton = Button(window, text="add", command=submit)
# addButton.pack()

# window.mainloop()




