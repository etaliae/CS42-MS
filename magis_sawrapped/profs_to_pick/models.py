from django.db import models
from schedo.models import Subject, Professor


# class Department(models.Model):
#     department_name = models.CharField(unique=True, max_length=150)

#     def __str__(self):
#         return self.department_name


# class Professor(models.Model):
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     last_name = models.CharField(max_length=150)
#     given_name = models.CharField(max_length=150)
#     middle_initial = models.CharField(max_length=5, blank=True, default='')

#     class Meta:
#         constraints = [models.UniqueConstraint(
#             fields=['last_name', 'given_name', 'middle_initial'],
#             name='prof_uniq')]
#         ordering = ['last_name']

#     def __str__(self):
#         return '{}, {} {}'.format(self.last_name, self.given_name, self.middle_initial)


class Review(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default='')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, default='')
    review = models.TextField()

    def __str__(self):
        return '{}'.format(self.review)
