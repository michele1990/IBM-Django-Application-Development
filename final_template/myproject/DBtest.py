import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

# from onlinecourse.models import Course, Question, Choice


# # Get all questions
# questions = Question.objects.all()

# # Print out course, text, and grade_point for each question
# for question in questions:
#     print(f'Course: {question.course.name}')
#     print(f'Text: {question.text}')
#     print(f'Grade Point: {question.grade_point}\n')


from onlinecourse.models import Course, Question, Choice


# Get all courses
courses = Course.objects.all()

# Print out the exam field for each course
for course in courses:
    if course.exam:
        print(f'Course: {course.name} has exam')
    else:
        print(f'Course: {course.name} does not have exam')
