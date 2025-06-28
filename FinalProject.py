import time
import math
print(" Welcome to The Mysterious Totem")
time.sleep(1)
print("The purpose of this game is to find the mystical totem!")
time.sleep(1)
print("While on the hunt, you will have to face three levels, each with jam-packed obstacles until you get the totem! ")
time.sleep(1)
health = 150
weapons = 2
name = input("Before we will start, we would like to know your name discoverer?" )
print("Greetings, "+ name +"!")
time.sleep(1)
print,(name,"Welcome to the game!")
time.sleep(1)
print("Let's begin")
time.sleep(1)
print("Here are somethings that you have in your inventory!")
time.sleep(1)
print("You start with 150 health.")
time.sleep(1)
print("2 weapons to start with until you reach the next three levels")
time.sleep(1)   
print("Choose a level:")
print("1: Cross Rapid Rivers")
print("2: Go through maze")
print("3: Fight star pirates")
time.sleep(1)
level = input("Enter the number of your choice: ")
choice = None 
print("Now choose a number 1, 2, 3")
if level == '1':
    print("Cross Rapid Rivers")
    time.sleep(1)
    print("You come to the ocean and see a boat sitting in the middle ")
    time.sleep(1)
    print("You swim towards until a rush of waves take you under")
    health -= 30 #Math operator
    time.sleep(1)
    print("Out of now where waves start rushing to you and take you under but luckily you find a shore.")
    time.sleep(1)
    print("You have lost 30 health points, you currently health: 120 ") 
elif level == '2':
    print("Go through maze")
    time.sleep(1)
    print("You appear through a portal and see a massive maze")
    time.sleep(1)
    print("There you see a backpack full of essentials and see a water bottle")
    health =+30 #Math operator
    time.sleep(1)
    print("You have gained 30 health points")
    time.sleep(1)
    print("You try to finish the maze but you cannot see the end so you use a parachute and land at the end of the maze")
    time.sleep(1)
if level == '3':
    print("Fight star pirates")
    time.sleep(1)
    print("Now you run to the end but see a fort ")
    time.sleep(1)
    choice = input("You see that it is blocking the way so you either flee or fight: ").lower()
    time.sleep(1)
if choice == 'flee': 
    print("You get defense mechanism which lets you get a shield to push and a staff to  hold of the pirates")
    time.sleep(1)
elif choice == 'fight':
    print("You get a sword and a gauntlet to fight the pirates and earn your vicotry")
    time.sleep(1)
    print("Invalid choice, please choose either 'flee' or 'fight'. ")
    time.sleep(1)
print("From there you have grabbed the totem and ran straight to the end.")
time.sleep(1)
print("You have successfully finished this mission")
time.sleep(1)
print("Thank you for playing the Mysterious Totem!")




