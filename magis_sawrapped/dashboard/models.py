from django.db import models
from django.urls import reverse
from schedo.models import SchoolYear, Subject


class Grade(models.Model):
    semester = models.ForeignKey(
        SchoolYear, on_delete=models.CASCADE, default='')
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, default='')
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
