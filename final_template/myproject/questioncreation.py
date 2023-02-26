

import random
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from onlinecourse.models import Course, Question, Choice


beginner_course = Course.objects.get(name='Python for Beginners')
intermediate_course = Course.objects.get(name='Python for Intermediate')
pro_course = Course.objects.get(name='Professional Python')

# Questions for Python for Beginners
beginner_questions = [
    {'question_text': 'What is the correct syntax to output "Hello World" in Python 3?',
     'choices': [
         {'choice_text': 'print("Hello World")', 'is_correct': True},
         {'choice_text': 'echo("Hello World")', 'is_correct': False},
         {'choice_text': 'echo "Hello World"', 'is_correct': False},
         {'choice_text': 'println("Hello World")', 'is_correct': False},
         {'choice_text': 'printf("Hello World")', 'is_correct': False},
     ]},
    {'question_text': 'Which of the following data types is NOT supported in Python?',
     'choices': [
         {'choice_text': 'integer', 'is_correct': False},
         {'choice_text': 'boolean', 'is_correct': False},
         {'choice_text': 'string', 'is_correct': False},
         {'choice_text': 'array', 'is_correct': True},
         {'choice_text': 'float', 'is_correct': False},
     ]},
    {'question_text': 'What is the correct way to define a function in Python?',
     'choices': [
         {'choice_text': 'def my_function:', 'is_correct': True},
         {'choice_text': 'define my_function:', 'is_correct': False},
         {'choice_text': 'function my_function:', 'is_correct': False},
         {'choice_text': 'my_function():', 'is_correct': False},
         {'choice_text': 'def function my_function:', 'is_correct': False},
     ]},
    {'question_text': 'What is the result of 7 % 3?',
     'choices': [
         {'choice_text': '2', 'is_correct': True},
         {'choice_text': '3', 'is_correct': False},
         {'choice_text': '1', 'is_correct': False},
         {'choice_text': '0', 'is_correct': False},
         {'choice_text': '4', 'is_correct': False},
     ]},
    {'question_text': 'What is the result of the following code? \n\nx = ["apple", "banana", "cherry"]\nprint(len(x))',
     'choices': [
         {'choice_text': '3', 'is_correct': True},
         {'choice_text': '4', 'is_correct': False},
         {'choice_text': '2', 'is_correct': False},
         {'choice_text': '1', 'is_correct': False},
         {'choice_text': '0', 'is_correct': False},
     ]},
]

# Questions for Python for Intermediate
intermediate_questions = [
    {'question_text': 'Which of the following is NOT a Python built-in data type?',
     'choices': [
         {'choice_text': 'int', 'is_correct': False},
         {'choice_text': 'str', 'is_correct': False},
         {'choice_text': 'bool', 'is_correct': False},
         {'choice_text': 'double', 'is_correct': True},
         {'choice_text': 'list', 'is_correct': False},
     ]},
    {'question_text': 'What is the correct way to open a file in Python?',
     'choices': [
     {'choice_text': 'file = open("filename.txt", "r")', 'is_correct': True},
     {'choice_text': 'file = open("filename.txt", "w")', 'is_correct': False},
     {'choice_text': 'file = open("filename.txt", "a")', 'is_correct': False},
     {'choice_text': 'file = open("filename.txt", "x")', 'is_correct': False},
     {'choice_text': 'file = open("filename.txt", "b")', 'is_correct': False},
 ]},
{'question_text': 'What is the result of the following code? \n\nx = {1, 2, 3}\nprint(type(x))',
 'choices': [
     {'choice_text': "<class 'set'>", 'is_correct': True},
     {'choice_text': "<class 'list'>", 'is_correct': False},
     {'choice_text': "<class 'tuple'>", 'is_correct': False},
     {'choice_text': "<class 'dict'>", 'is_correct': False},
     {'choice_text': "<class 'int'>", 'is_correct': False},
 ]},
{'question_text': 'What is the correct way to inherit from a class in Python?',
 'choices': [
     {'choice_text': 'class ChildClass(ParentClass):', 'is_correct': True},
     {'choice_text': 'class ChildClass extends ParentClass:', 'is_correct': False},
     {'choice_text': 'class ChildClass implements ParentClass:', 'is_correct': False},
     {'choice_text': 'class ChildClass inherits ParentClass:', 'is_correct': False},
     {'choice_text': 'class ChildClass is ParentClass:', 'is_correct': False},
 ]},
{'question_text': 'What is the result of the following code? \n\nx = [1, 2, 3]\ny = x\ny.append(4)\nprint(x)',
 'choices': [
     {'choice_text': '[1, 2, 3, 4]', 'is_correct': True},
     {'choice_text': '[1, 2, 3]', 'is_correct': False},
     {'choice_text': '[1, 2, 3, 4, 4]', 'is_correct': False},
     {'choice_text': '[1, 2, 3, [4]]', 'is_correct': False},
     {'choice_text': 'Error', 'is_correct': False},
 ]},
{'question_text': 'Which of the following is NOT a Python comparison operator?',
 'choices': [
     {'choice_text': '<>', 'is_correct': True},
     {'choice_text': '==', 'is_correct': False},
     {'choice_text': '!=', 'is_correct': False},
     {'choice_text': '>', 'is_correct': False},
     {'choice_text': '<=', 'is_correct': False},
 ]},
]



# Questions for Python PRO

pro_questions = [
{'question_text': 'What is the output of the following code? \n\nx = [1, 2, 3, 4, 5]\ny = [i for i in x if i % 2 == 0]\nprint(y)',
'choices': [
{'choice_text': '[2, 4]', 'is_correct': True},
{'choice_text': '[1, 3, 5]', 'is_correct': False},
{'choice_text': '[1, 2, 3, 4, 5]', 'is_correct': False},
{'choice_text': '[1, 2, 3, 4]', 'is_correct': False},
{'choice_text': '[4, 2]', 'is_correct': False},
]},
{'question_text': 'What is the result of the following code? \n\nx = {"apple": 1, "banana": 2, "cherry": 3}\nfor key, value in x.items():\n print(key, value)',
'choices': [
{'choice_text': 'apple 1\nbanana 2\ncherry 3', 'is_correct': True},
{'choice_text': '1 apple\n2 banana\n3 cherry', 'is_correct': False},
{'choice_text': '["apple", 1]\n["banana", 2]\n["cherry", 3]', 'is_correct': False},
{'choice_text': '["apple", 1], ["banana", 2], ["cherry", 3]', 'is_correct': False},
{'choice_text': 'Error', 'is_correct': False},
]},
{'question_text': 'What is the correct way to sort a list in descending order in Python?',
'choices': [
{'choice_text': 'my_list.sort(reverse=True)', 'is_correct': True},
{'choice_text': 'my_list.sort(reverse)', 'is_correct': False},
{'choice_text': 'my_list.sort_desc()', 'is_correct': False},
{'choice_text': 'my_list.desc_sort()', 'is_correct': False},
{'choice_text': 'my_list.reverse()', 'is_correct': False},
]},
{'question_text': 'What is the result of the following code? \n\nx = lambda a, b: a * b\nprint(x(5, 6))',
'choices': [
{'choice_text': '30', 'is_correct': True},
{'choice_text': '11', 'is_correct': False},
{'choice_text': '56', 'is_correct': False},
{'choice_text': '0.8333333333333334', 'is_correct': False},
{'choice_text': 'Error', 'is_correct': False},
]},
{'question_text': 'What is the correct way to define a variable as a constant in Python?',
'choices': [
{'choice_text': 'There is no way to define a variable as a constant in Python', 'is_correct': True},
{'choice_text': 'Use the "const" keyword', 'is_correct': False},
{'choice_text': 'Use the "let" keyword', 'is_correct': False},
{'choice_text': 'Use the "var" keyword', 'is_correct': False},
{'choice_text': 'Use all uppercase letters for the variable name', 'is_correct': False},
]},
]

#Save the questions to the database


for question_data in beginner_questions:
    question = Question.objects.create(course=beginner_course, text=question_data['question_text'],grade_point=1)
    print("oi")
    for choice_data in question_data['choices']:
        Choice.objects.create(question=question, text=choice_data['choice_text'], is_correct=choice_data['is_correct'])
        print("hey")



for question_data in intermediate_questions:
    question = Question.objects.create(course=intermediate_course, text=question_data['question_text'],grade_point=1)
    print("oi")
    for choice_data in question_data['choices']:
        Choice.objects.create(question=question, text=choice_data['choice_text'], is_correct=choice_data['is_correct'])
        print("hey")


for question_data in pro_questions:
    question = Question.objects.create(course=pro_course, text=question_data['question_text'],grade_point=1)
    print("oi")
    for choice_data in question_data['choices']:
        Choice.objects.create(question=question, text=choice_data['choice_text'], is_correct=choice_data['is_correct'])
        print("hey")