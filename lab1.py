import math



# TASK 1


print("----- TASK 1 -----")

name = input("What is your name?\n")
print(f"Hello {name}.")

student_id = input("What is your Student ID?\n")
print(f"Your ID is {student_id}.")



# TASK 2 - Time Logic


print("\n----- TASK 2 -----")

total_seconds = int(input("Enter total seconds:\n"))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} seconds is {hours} hours, {minutes} minutes, and {seconds} seconds.")



# TASK 3 


print("\n----- TASK 3 -----")

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The distance between the points is {distance}")



# TASK 4 


print("\n----- TASK 4 -----")

print("*******\n *****\n  ***\n   *")
