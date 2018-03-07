print ("hello world")
print ("xxxxxxxxxxx")

def add_numbers1(a, b, c):
    print (a+b+c)
add_numbers1(5,689,1)
add_numbers1(19, 10, 15)

answer = 4
pi = 3.14159

print (answer + pi)

int(pi)
float(answer)

#'Hello World' == "Hello World" == """Hello World"""

#"hello".capitalize() == "Hello"
#"hello".replace("e", "a") == "hallo"
#"hello".isalpha() == True
#"123".isdigit() == True# Useful when converting to int
#"some,csv,values".split(",") == ["some", "csv", "values"]

#name = "PythonBo"

#machine = "HAL"
#"Nice to meet you {0}. I am {1}".format(name, machine)
#f"Niceto meet you {name}. I am {machine}"


#python_course= True
#java_course= False
#int(python_course) == 1
#int(java_course) == 0
#str(python_course) == "True"
#aliens_found= None

print ('looking for number ?')
number = 15
if number == 5:
    print("Number is 5")
else: print("Number is NOT 5")

number = 5
if number:
    print("Number is defined and truthy")
    text = "Python"
if text:
    print("Text is defined and truthy")

python_course= 1
if python_course: # Not python_course== True
   print("This will execute")

aliens_found= 1
if aliens_found:
   print("This will NOT execute")

number = 6
if number != 5:
    print("This will not execute")


number = 3
python_course = True
if number == 3 and python_course:
    print("This will execute")
 if number == 17 or python_course:
    print("This will also execute")


#a = -1
#b = 2
#"bigger" ifa > b else"smaller"

student_names= []
student_names= ["Mark", "Katarina", "Jessica"]
student_names[0] == 'Mark'
print(student_names[0])
student_names[0] = 'Jack'
print(student_names[0])

student_names = ["Mark", "Katarina", "Jessica"]
student_names[3] = "Homer" # No can do!
student_names.append("Homer") # Add to the end
student_names == ["Mark", "Katarina", "Jessica", "Homer"]
"Mark" in student_names == True # Mark is still there!
len(student_names) == 4 # How many elements in the list
del student_names[2] # Jessica is no longer in the list :(
student_names = ["Mark", "Katarina", "Homer"]
student_names[1:] == ["Katarina", "Homer"]
student_names[1:-1] == ["Katarina"]


student = {
    "name": "Mark",
    "student_id": 15163,
    "feedback": None
}
student = {
    "name": "Katarina",
    "student_id": 63221,
    "feedback": None
}

all_students = [
    {"name": "Mark", "student_id": 15163},
    {"name": "Katarina", "student_id": 63221},
    {"name": "Jess", "student_id": 30021}
]

all_students['name'] == "Mark"
student["last_name"] == KeyError
student.get("last_name", "Unknown") == "Unknown"
student.keys() = ["name", "student_id", "feedback"]
student.values() = ["Mark", 15163, None]
student["name"] = "James"
del student["name"]

tuple= (3, 5, 1, "Mark")

set and frozenset
set([3, 2, 3, 1, 5]) == (1, 2, 3, 5)

print("Hello World")
str(3) == "3"
int("15") == 15
username = input("Enter the user's name: ")

def get_students():
    students = ["mark", "james"]
    def get_students_titlecase():
        students_titlecase = []
        for student in students:
            students_titlecase.append(student.title())
        return student_titlecase
    students_titlecase_names = get_titlecase_names()
    print(students_titlecase_names)

def double (x):
    return x *2
double(10)



