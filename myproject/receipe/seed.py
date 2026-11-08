from faker import Faker
import random

from .models import *

fake = Faker()


def seed_db(n=100) -> None:

    for i in range(n):

        try:
            department_obj = Department.objects.all()

            random_index = random.randint(0, len(department_obj) - 1)
            department = department_obj[random_index]

            student_id = f'STU_{random.randint(100, 999)}'
            student_name = fake.name()
            student_age = random.randint(18, 30)
            student_address = fake.address()

            student_id_no = StudentId.objects.create(
                student_id=student_id
            )

            Student.objects.create(
                department=department,
                student_id=student_id_no,
                student_name=student_name,
                student_age=student_age,
                student_address=student_address
            )

        except Exception as e:
            print(e)
