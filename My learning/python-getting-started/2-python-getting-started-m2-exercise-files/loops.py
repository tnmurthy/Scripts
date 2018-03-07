# import numpy as np

student_names = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]

for name in student_names:
    if name == "James":
        continue
        print("Found him!" + name)
    print("Currently testing " + name)

#infinite loop
#x = 0
#while x < 10:
#    print("Count is {0}".format(x))
#x+= 1

#num = 10
#while True:
#    if num == 42:
#        break
#        print ("Hello World")