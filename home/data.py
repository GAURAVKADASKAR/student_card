from home.models import *
from random import randint
from faker import Faker
fake=Faker()
def student_data(n=10):

    for i in range(0,n):
        department_obj=DEPARTMENT.objects.all()
        department_index=randint(0,len(department_obj)-1)
        department=department_obj[department_index]
        index=randint(101,1000)
        student_id=f'stu-{index}'
        student_name=fake.name()
        student_email=fake.email()
        student_age=randint(18,25)
        student_addre=fake.address()
        dd=DEPARTMENT.objects.create(
            department=department
        )
        ss=STUDENTID.objects.create(
            student_id=student_id
        )
        stt=STUDENT.objects.create(
            department=dd,
            student_id=ss,
            student_name=student_name,
            student_email=student_email,
            student_age=student_age,
            student_addre=student_addre
        )
def Marks_data(n=10):
    stu=STUDENT.objects.all()
    for students in stu:
        mm=SUBJECT.objects.all()
        for subjects in mm:
            tt=SUBJECTMARKS.objects.create(
                student=students,
                subject=subjects,
                mark=randint(0,100)
            )

