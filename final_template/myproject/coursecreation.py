import random
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

from onlinecourse.models import Course, Lesson

# Define the courses and their descriptions
courses = [
    {'name': 'Python for Beginners', 'description': 'This course is designed for students who have no previous programming experience.'},
    {'name': 'Python for Intermediate Learners', 'description': 'This course is designed for students who have some experience with Python programming.'},
    {'name': 'Professional Python', 'description': 'This course is designed for students who want to take their Python skills to the next level.'}
]

# Define the lessons for each course
lessons = [
    # Python for Beginners lessons
    [{'name': 'Introduction to Python', 'description': 'This lesson covers the basics of Python programming.'},
     {'name': 'Data Types and Variables', 'description': 'This lesson covers the different data types and variables in Python.'},
     {'name': 'Conditional Statements', 'description': 'This lesson covers how to use conditional statements in Python.'},
     {'name': 'Loops', 'description': 'This lesson covers how to use loops in Python.'},
     {'name': 'Functions', 'description': 'This lesson covers how to define and use functions in Python.'},
     {'name': 'Lists', 'description': 'This lesson covers how to use lists in Python.'},
     {'name': 'Dictionaries', 'description': 'This lesson covers how to use dictionaries in Python.'},
     {'name': 'Modules and Packages', 'description': 'This lesson covers how to use modules and packages in Python.'},
     {'name': 'File Handling', 'description': 'This lesson covers how to handle files in Python.'},
     {'name': 'Error Handling', 'description': 'This lesson covers how to handle errors in Python.'}],

    # Python for Intermediate Learners lessons
    [{'name': 'Advanced Data Types', 'description': 'This lesson covers advanced data types and how to use them in Python.'},
     {'name': 'Object-Oriented Programming', 'description': 'This lesson covers the principles of object-oriented programming in Python.'},
     {'name': 'Inheritance and Polymorphism', 'description': 'This lesson covers how to use inheritance and polymorphism in Python.'},
     {'name': 'Exception Handling', 'description': 'This lesson covers advanced error handling in Python.'},
     {'name': 'Generators', 'description': 'This lesson covers how to use generators in Python.'},
     {'name': 'Regular Expressions', 'description': 'This lesson covers how to use regular expressions in Python.'},
     {'name': 'Database Programming', 'description': 'This lesson covers how to interact with databases in Python.'},
     {'name': 'Web Development with Python', 'description': 'This lesson covers how to build web applications with Python.'},
     {'name': 'Testing and Debugging', 'description': 'This lesson covers how to test and debug Python code.'},
     {'name': 'Best Practices', 'description': 'This lesson covers best practices for Python programming.'}],

    # Professional Python lessons
    [{'name': 'Data Analysis with Python', 'description': 'This lesson covers how to analyze data using Python.'},
     {'name': 'Machine Learning with Python', 'description': 'This lesson covers how to use machine learning algorithms with Python.'},
     {'name': 'Web Scraping with Python', 'description': 'This lesson covers how to scrapewebsites using Python.'},
    {'name': 'Network Programming', 'description': 'This lesson covers how to build networked applications using Python.'},
    {'name': 'Parallel and Concurrent Programming', 'description': 'This lesson covers how to write concurrent and parallel programs in Python.'},
    {'name': 'Debugging and Profiling', 'description': 'This lesson covers how to debug and profile Python code.'},
    {'name': 'Cython and C Extensions', 'description': 'This lesson covers how to use Cython and C extensions to speed up Python code.'},
    {'name': 'Collaborative Software Development with Python', 'description': 'This lesson covers how to collaborate on software development projects using Python.'},
    {'name': 'Packaging and Distribution', 'description': 'This lesson covers how to package and distribute Python applications.'},
    {'name': 'Advanced Best Practices', 'description': 'This lesson covers advanced best practices for Python programming.'}]
]


    
for i in range(len(courses)):
    course = Course.objects.create(name=courses[i]['name'], description=courses[i]['description'])
    print(f"Course created: {course.name}")
    for j in range(len(lessons[i])):
        lesson = Lesson.objects.create(title=lessons[i][j]['name'], content=lessons[i][j]['description'], course=course)
        print(f"Lesson created: {lesson.title}")
