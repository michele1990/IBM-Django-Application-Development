import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
import django
django.setup()

import random
from django.contrib.auth.models import User

# A list of common first and last names to choose from
first_names = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia', 'Mia', 'Charlotte', 'Amelia', 'Evelyn', 'Abigail']
last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']

# Generate 15 random users with common first and last names
for i in range(15):
    # Choose a random first name and last name
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)

    # Generate a unique username by combining the first and last name
    username = f"{first_name.lower()}.{last_name.lower()}{i+1}"

    # Create a new user with the random name and password "northwestwind"
    user = User.objects.create_user(username=username, password='northwestwind', first_name=first_name, last_name=last_name)
    print(f"User created: {user.username}")
