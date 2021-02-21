#Section C

import random
import string
import collections

NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4  # 3 choices is A/B/C, 4 choices is A/B/C/D, 5 is A/B/C/D/E

#Section C.1

def generate_answers(num_questions, num_choice):
    """Return str of answers based on number of questions, and number of choices"""
    choices = list(string.ascii_uppercase[:num_choice])
    answers = ''
    for i in range(num_questions):
        temp = random.choice(choices)
        answers = "{}{}".format(answers, temp)
    return answers


ANSWERS = generate_answers(NUMBER_OF_QUESTIONS, NUMBER_OF_CHOICES)
##print(ANSWERS)


#Section C.2
Student = collections.namedtuple('Student', 'name answers scores total')


##def random_students(num_students):
##    """Return list of Student (random name, random answers) based on number of students"""
##    student_list = []
##    for i in range(num_students):
##        temp_id = str(random.randrange(1, 9999)).zfill(4)
##        student_answers = generate_answers(NUMBER_OF_QUESTIONS, NUMBER_OF_CHOICES)
##        new_student = Student(temp_id, student_answers, score, grade)
##        student_list.append(new_student)
##    return student_list


#Section C.3
def check_answers(student_answer:str, answer_key:str):
    """Check answers against answer key, and return list of correct (1) or incorrect(0)"""
    student = list(student_answer)
    answer_key = list(ANSWERS)
    correct = []
    for i in range(len(answer_key)):
        if student[i] == answer_key[i]:
            correct.append(1)
        else:
            correct.append(0)
    return correct


def total(correct_list):
    """Return total of check_answers list"""
    score = sum(correct_list, 0)
    return score


def score_student(s: Student, answer_key):
    """Returns a student with score and total"""
    score = check_answers(s.answers, ANSWERS)
    grade = total(score)
    graded_student = Student(s.name, s.answers, score, grade)
    return graded_student


def print_list(List: list, num: int):
    """print list of students"""
    for i in range(num):
        temp = List[i]
        print(temp)
        

def random_students(num_students):
    """Return list of Student (random name, random answers) based on number of students"""
    student_list = []
    for i in range(num_students):
        temp_id = str(random.randrange(1, 9999)).zfill(4)
        student_answers = generate_answers(NUMBER_OF_QUESTIONS, NUMBER_OF_CHOICES)
        score = check_answers(student_answers, ANSWERS)
        grade = total(score)
        new_student = Student(temp_id, student_answers, score, grade)
        student_list.append(new_student)
    return student_list


def sort_key_total(s: Student):
    """Return total of student"""
    return s.total

print('-Random Student Choices-')
Student_list = random_students(NUMBER_OF_STUDENTS)
Student_list.sort(key=sort_key_total, reverse = True)
print_list(Student_list, 10)


def average_score(SL: list):
    """Return average of totals in list of students"""
    total = 0
    for i in range(len(SL)):
        temp = SL[i]
        score = temp.total
        total = total + score
    students = len(SL)
    avg = total / students
    return avg

print(average_score(Student_list))
print('\n\n')


# Section C.4

def generate_weighted_student_answer(correct_answer:str):
    """Return single answer based on a weighted choice"""
    student_choices = list(string.ascii_uppercase[:NUMBER_OF_CHOICES])
    student_choices.append(correct_answer)
    student_answer = random.choice(student_choices)
    return student_answer

##print(generate_weighted_student_answer('C'))

def student_answers(answer_key):
    """Return string of student answer using a weighted answer"""
    answer_key = list(answer_key)
    student_answers = ''
    for i in range(len(answer_key)):
        temp = answer_key[i]
        current_answer = generate_weighted_student_answer(temp)
        student_answers = "{}{}".format(student_answers, current_answer)
    return student_answers

##test1 = student_answers(ANSWERS)
##print(test1)
        

def random_students2(num_students):
    """Return list of Student (random name, random answers) based on number of students"""
    student_list = []
    for i in range(num_students):
        temp_id = str(random.randrange(1, 9999)).zfill(4)
        student_answer = student_answers(ANSWERS)
        score = check_answers(student_answer, ANSWERS)
        grade = total(score)
        new_student = Student(temp_id, student_answer, score, grade)
        student_list.append(new_student)
    return student_list


print('-Weighted Student Choices-')
Student_list2 = random_students2(NUMBER_OF_STUDENTS)
Student_list2.sort(key=sort_key_total, reverse = True)
print_list(Student_list2, 10)
print(average_score(Student_list2))
print('\n\n')


# Section C.5

def question_weights(SL):
    """Returns a list of number of incorrect answers by student per question"""
    incorrect_answers = []
    for i in range(NUMBER_OF_QUESTIONS):
        incorrect_num = incorrect_per_question(SL, i)
        incorrect_answers.append(incorrect_num)
    return incorrect_answers
        


def incorrect_per_question(SL: list, question:int):
    """Return number of incorrent answers from student for individual question"""
    answers_for_question = []
    correct = 0
    for i in range(len(SL)):
        student = SL[i]
        question = student.scores[question]
        correct = question + correct
    incorrect = len(SL) - correct
    return incorrect

##test2 = incorrect_per_question(Student_list2, 0)
##print(test2)

QUESTION_WEIGHTS = question_weights(Student_list2)
##print(test3)


def Student_weight_scores(s: Student, question_weights):
    """Returns students weighted score based on questions weights"""
    score = s.scores
    weighted_score = []
    for i in range(len(question_weights)):
        current_score = score[i]
        current_weight = question_weights[i]
        weight_adj = (current_score * current_weight) / NUMBER_OF_STUDENTS
        weighted_score.append(weight_adj)
    return weighted_score

##test4 = Student_weight_scores(Student_list2[0], QUESTION_WEIGHTS)
##print(test4)
##print(sum(test4,0)/NUMBER_OF_STUDENTS)


def weight_adj(SL):
    for i in range(len(SL)):
        student = SL[i]
        weighted_score = Student_weight_scores(student, QUESTION_WEIGHTS)
        weighted_student = Student(student.name, student.answers, weighted_score, sum(weighted_score,0))
        SL[i] = weighted_student
    return SL
    


print('-Weighted Questions-')
Student_list3 = weight_adj(Student_list2)
Student_list3.sort(key=sort_key_total, reverse = True)
print_list(Student_list3, 10)
print(average_score(Student_list3))
print('\n\n')




## Section D

# Section D.1a

POINTS = {'A':4, 'B':3, 'C':2, 'D':1, 'F':0}

def calculate_GPA(grades):
    """Takes a string of letters, and returns the grade point average"""
    total_points = 0
    for grade in grades:
        current = POINTS[grade]
        total_points = total_points + current
    gpa = total_points / len(grades)
    return gpa


# Section D.1b

def calculate_GPA2(grade_list):
    """Takes a string of letters, and returns the grade point average"""
    total_points = 0
    for grade in grade_list:
        current = POINTS[grade]
        total_points = total_points + current
    gpa = total_points / len(grade_list)
    return gpa

assert calculate_GPA(['A', 'C', 'A', 'B', 'A', 'F', 'D']) == 2.5714285714285716
assert calculate_GPA2(['A', 'C', 'A', 'B', 'A', 'F', 'D']) == 2.5714285714285716


# Section D.2

def flatten_2D_list(list_of_list: list):
    """Return one level list from a list of list"""
    D1_list = []
    for items in list_of_list:
        D1_list.extend(items)
    return D1_list

assert flatten_2D_list([[1, 3, 2], [3, 5, 1], [7, 5, 1], [3, 2], [9, 4]]) == [1, 3, 2, 3, 5, 1, 7, 5, 1, 3, 2, 9, 4]


# Section D.3a

L = ['If', 'you', '432234', 'did', 'the', '9834234', 'exercise', 'correctly', '534523423',
     'this', 'should', '1044323', 'be', 'readable']

def skip_every_third_item(sl: list):
    """Print every item except for every third item"""
    for i in range(len(sl)):
        line = i + 1
        current = sl[i]
        if line%3 != 0:
            print(current)

skip_every_third_item(L)


# Section D.3b

def skip_every_nth_item(sl: list, skip:int):
    """Print every line except for every nth item"""
    for i in range(len(sl)):
        line = i + 1
        current = sl[i]
        if line%skip != 0:
            print(current)

skip_every_nth_item(L, 3)


# Section D.4a

work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob', 
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']

def tally_days_worked(employees: list):
    """Return dictionary of the count of how many days worked for each employee"""
    worked_counter = {}
    for employee in employees:
        if employee not in worked_counter.keys():
            worked_counter[employee] = 1
        elif employee in worked_counter.keys():
            worked_counter[employee] = worked_counter[employee] + 1
    return worked_counter

workers = tally_days_worked(work_week)
print(workers)


# Section D.4b

hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50, 'Bob': 30.00,
                'Samantha': 8.50, 'Larry': 8.50, 'Huey': 18.00}

daily_hr = 8

def pay_employees(EL: list, hourly_wage):
    """Print passage describing employee, hrs worked, amt due, hrly rate"""
    employees_worked = EL.keys()
    for employee in employees_worked:
        amt_due = workers[employee] * hourly_wage[employee] * daily_hr
        due_str = "{} will be paid ${:.2f} for {} hours of work at ${:.2f} per hour.\n".format(
            employee, amt_due, (workers[employee] * daily_hr), hourly_wage[employee])
        print(due_str)

pay_employees(workers, hourly_wages)
            

# Section d.5

def reverse_dict(dictionary):
    """Return new dictionary where value and key of orignal dictionary is reversed"""
    values = list(dictionary.values())
    keys = list(dictionary.keys())
    reverse_dict = {}
    for i in range(len(dictionary)):
        current_value = values[i]
        current_key = keys[i]
        reverse_dict[current_value] = current_key
    return reverse_dict  


new_dict = reverse_dict({'a': 'one', 'b': 'two', 'c': 'three', 'd': 'four', 'e': 'five', 'f': 'six'})
print(new_dict)
