from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Subject(models.Model):
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


class SchoolYear(models.Model):
    school_year = models.CharField(unique=True, max_length=150)

    def __str__(self):
        return '{}'.format(self.school_year)

    class Meta:
        ordering = ['school_year']


class Semester(models.Model):
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
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


class Grade(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    GRADE_CHOICES = (
        ("A", "A"),
        ("B+", "B+"),
        ("B", "B"),
        ("C+", "C+"),
        ("C", "C"),
        ("D", "D"),
        ("F", "F"),
        ("S", "S"),
        ("WP", "WP"),
    )
    grade = models.CharField(max_length=2, choices=GRADE_CHOICES, default='A')

    class Meta:
        constraints = [models.UniqueConstraint(
            fields=['semester', 'subject'],
            name='sem_and_sub__uniq')]
        ordering = ['-semester', 'grade']

    def __str__(self):
        return '{}'.format(self.grade)

    def get_absolute_url(self):
        return reverse('dashboard:grades-list')
