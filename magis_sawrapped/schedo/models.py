from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# from profs_to_pick.models import Professor

class Department(models.Model):
    department_name = models.CharField(unique=True, max_length=150)
    
    def __str__(self):
        return self.department_name

class Subject(models.Model): # Subject is equivalent to course
    subject_code = models.CharField(primary_key=True, max_length=20)
    course_title = models.CharField(max_length=150)
    units = models.IntegerField(default=0,
                                validators=[MaxValueValidator(6),
                                            MinValueValidator(0)])

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['subject_code', 'course_title', 'units'],
            name='subj_uniq')]
        ordering = ['subject_code']

    def __str__(self):
        return '{}: {}'.format(self.subject_code, self.course_title)
    
class Professor(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default='')
    last_name = models.CharField(max_length=150)
    given_name = models.CharField(max_length=150)
    middle_initial = models.CharField(max_length=5, blank=True, default='')

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['last_name', 'given_name', 'middle_initial'],
            name='prof_uniq')]
        ordering = ['last_name']

    def __str__(self):
        return '{}, {} {}'.format(self.last_name, self.given_name, self.middle_initial)

class SchoolYear(models.Model):
    school_year = models.CharField(unique=True, max_length=150)
    SEMESTER_CHOICES = (
        ("0", "Intersession"),
        ("1", "First Semester"),
        ("2", "Second Semester"),
    )
    semester = models.CharField(max_length=20,
                                choices=SEMESTER_CHOICES,
                                default='0')

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['school_year', 'semester'],
            name='sy_and_sem_uniq')]
        ordering = ['-school_year', '-semester']

    def __str__(self):
        return '{}-{}'.format(self.school_year, self.semester)


# class Semester(models.Model):
#     school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    
class Time(models.Model):
    time = models.CharField(max_length=9) # XXXX-XXXX
    day = models.CharField(max_length=10)
    room = models.CharField(max_length=20)
    modality = models.CharField(max_length=20)

class Schedule(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        default=''
    )
    time = models.ForeignKey(
        Time,
        on_delete=models.CASCADE,
        default=''
    )
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        default=''
    )
    section = models.CharField(max_length=10)
    max_no = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    lang = models.CharField(max_length=3)
    level = models.CharField(max_length=1)
    free_slots = models.IntegerField()
    remarks = models.CharField(max_length=200)
    s = models.CharField(max_length=1)
    p = models.CharField(max_length=1)