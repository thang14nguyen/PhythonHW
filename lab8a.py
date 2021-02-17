## LAB 8

## Section C

#Section C.1

import collections
Dish = collections.namedtuple('Dish', 'dish price calories')

def read_menu_with_count(file_name:str):
    "Take file name as string, and return list of Dish"
    file = open(file_name).read()
    dishes = file.split(sep='\n')
    dishes = dishes[1:]
    num_of_dish = len(dishes)
    menu = []
    for index in range(num_of_dish):
        current_dish = dishes[index]
        current_dish = current_dish.split(sep = '\t')
        dish = current_dish[0]
        price = float(current_dish[1].replace('$', ''))        
        calories = float(current_dish[2])
        menu_item = Dish(dish, price, calories)
        menu.append(menu_item)
    return menu


print(read_menu_with_count('menu1.txt'))
print(read_menu_with_count('menu2.txt'))


#Section C.2
def read_menu(file_name:str):
    "Take file name as string, and return list of Dish"
    file = open(file_name).read()
    dishes = file.split(sep='\n')
    ##dishes = dishes[1:]
    num_of_dish = len(dishes)
    menu = []
    for index in range(num_of_dish):
        current_dish = dishes[index]
        current_dish = current_dish.split(sep = '\t')
        dish = current_dish[0]
        price = float(current_dish[1].replace('$', ''))        
        calories = float(current_dish[2])
        menu_item = Dish(dish, price, calories)
        menu.append(menu_item)
    return menu

dishes = (read_menu('menu3.txt'))


#Section C.3
def write_menu(list_of_dish:list, file_name:str):               #Is the styling correct? It should be list_of_Dish
    "Takes a list of dish, and writes to text file"
    file_length = len(list_of_dish)
    str_to_write = ''
    for index in range(file_length):
        current_dish = list_of_dish[index]
        current_dish_str = "{}\t${:.2f}\t{}".format(current_dish.dish, current_dish.price, int(current_dish.calories))
        str_to_write = "{}\n{}".format(str_to_write, current_dish_str)
    write_to_file = str(file_length) + str_to_write
    outfile = open(file_name, 'w', encoding='utf8')
    outfile.write(write_to_file)

write_menu(dishes, 'menu4.txt')
        

##Section D

Course = collections.namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)
  
Student = collections.namedtuple('Student', 'ID name level major studylist')
# All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])
sV = Student('41223344', 'Programmer, Virgina', 'SR', 'ICS', [ics31, mgt1])
  
StudentBody = [sW, sX, sY, sZ, sV]


#Section D.1
def Students_at_level(list_of_Students:list, class_lvl:str):
    "Take a list of Students, and returns list of Studens who's class lvl matches"
    student_match = []
    for index in range(len(list_of_Students)):
        current_student = list_of_Students[index]
        if current_student.level == class_lvl:
            student_match.append(current_student)
    return student_match

print('\n\n')
print(Students_at_level(StudentBody,'FR'))


#Section D.2
def Students_in_majors(list_of_Students:list, major:str):
    "Take a list of Students, and returns list of Studens who's major matches"
    student_match = []
    for index in range(len(list_of_Students)):
        current_student = list_of_Students[index]
        if current_student.major == major:
            student_match.append(current_student)
    return student_match

print('\n\n')
print(Students_in_majors(StudentBody,'PSB'))


#Section D.3
def Course_equals(c1: Course, c2: Course) -> bool:
    ''' Return True if the department and number of c1 match the department and
	     number of c2 (and False otherwise)
    '''
    match = 0
    if c1.dept == c2.dept:
        match = match + 1
    if c1.num == c2.num:
        match = match + 1
    return match == 2

    
def Course_on_studylist(c: Course, SL: 'list of Course') -> bool:
    ''' Return True if the course c equals any course on the list SL (where equality
	     means matching department name and course number) and False otherwise.
    '''
    match = 0
    for index in range(len(SL)):
        current_course = SL[index]
        if Course_equals(c, current_course):
            match = match + 1
    return match >= 1

assert Course_on_studylist(ics31, sW.studylist)
assert not Course_on_studylist(wr39b, sW.studylist)


def Student_is_enrolled(S: Student, department: str, coursenum: str) -> bool:
    ''' Return True if the course (department and course number) is on the student's
	     studylist (and False otherwise)
    '''
    match = False
    for index in range(len(S.studylist)):
        current_course = S.studylist[index]
        if department == current_course.dept:
            if coursenum == current_course.num:
                match = True
    return match

assert Student_is_enrolled(sW, 'ICS', '31')


def Student_in_class(SL: list, dept: str, num: str):
    """Returns a list of student who are enrolled in stated class based on dept and class num"""
    student_match = []
    for index in range(len(SL)):
        current_student = SL[index]
        if Student_is_enrolled( current_student, dept, num):
            student_match.append(current_student)
    return student_match

print('\n\n')
print (Student_in_class(StudentBody, 'ICS', '31'))
                

#Section D.4
def Student_names(SL: list):
    """Returns list of name from list of Students"""
    names = []
    for index in range(len(SL)):
        current_student = SL[index]
        names.append(current_student.name)
    return(names)

print ('\n\n')
print (Student_names(StudentBody))


#Section D.5
majors = ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']

def Students_in_ICS(SL: list):
    """Returns list of student with majors from school of ICS"""
    students = []
    for index in range(len(SL)):
        current_student = SL[index]
        if current_student.major in majors:
            students.append(current_student)
    return students

print ('\n\n')
print (Students_in_ICS(StudentBody))


def names_in_ICS(SL:list):
    """Return list of name from student in school of ICS"""
    students = Students_in_ICS(SL)
    names = Student_names(students)
    return(names)

print ('\n\n')
print (names_in_ICS(StudentBody))


def number_in_ICS(SL:list):
    students = len(Students_in_ICS(SL))
    return students

print ('\n\n')
print (number_in_ICS(StudentBody))


def senior_in_ICS(SL:list):
    sr_student = []
    students = Students_in_ICS(SL)
    for index in range(len(students)):
        current_student = students[index]
        if current_student.level == 'SR':
            sr_student.append(current_student)
    return sr_student

print ('\n\n')
print (senior_in_ICS(StudentBody))


def sr_num_ICS(SL:list):
    sr_num = len(senior_in_ICS(SL))
    return sr_num

print ('\n\n')
print (sr_num_ICS(StudentBody))


def percent_sr_ICS(SL: list):
    students = number_in_ICS(SL)
    seniors = sr_num_ICS(SL)
    return seniors / students

print ('\n\n')
print (percent_sr_ICS(StudentBody))

## Section E

#Section E.1
