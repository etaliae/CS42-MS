import pandas as pd
from django.db.models import Q
from .models import Grade

not_part_of_qpi = ['PHYED', 'NSTP', 'MATH 1.1', 'MATH 1.2',
                   'ENGL 9', 'ENGL 10', 'ENGL 10.1', 'FILI 10']
letters = {'A': 4.00, 'B+': 3.50, 'B': 3.00, 'C+': 2.50,
           'C': 2.00, 'D': 1.00, 'F': 0.00, 'W': 0.00}
honors_dict = {
    "Summa Cum Laude": [3.87, 4.00],
    "Magna Cum Laude": [3.70, 3.86],
    "Cum Laude": [3.50, 3.69],
    "Honorable Mention": [3.35, 3.49]
}


def get_grades():
    query = Q()

    # Removes grades that are not part of the QPI
    for entry in not_part_of_qpi:
        query = query | Q(subject__subject_code__contains=entry)

    # Removes grades that are either S or WP
    query = query | Q(grade__in=['S', 'WP'])

    # Holds grades part of QPI calculation
    included_grades = Grade.objects.exclude(query)

    # Specifies the fields to be included in the dataframe
    grades_data = included_grades.values('semester__school_year',
                                         'semester__semester',
                                         'subject__subject_code',
                                         'subject__units',
                                         'grade')

    # Places the database into a dataframe and remanes each column
    grades_df = pd.DataFrame(list(grades_data)).rename(columns={'semester__school_year': 'School Year',
                                                                'semester__semester': 'Sem',
                                                                'subject__subject_code': 'Subject Code',
                                                                'subject__units': 'Units',
                                                                'grade': 'Final Grade'})

    grades_df['Semester'] = grades_df['School Year'] + '-' + grades_df['Sem']

    final_gdf = grades_df[['Semester', 'Subject Code', 'Units', 'Final Grade']]

    return final_gdf


class Grades:  # Change later to enable other features
    def __init__(self):
        # Table of included grades in QPI computations
        self.df = get_grades()

        # Latest semester
        self.last_sem = self.df.iloc[-1]['Semester']

        # Number of semesters included in the table
        self.num_sem = self.df['Semester'].nunique()

        # Previous semester/s
        if self.num_sem < 2:
            self.df_delta = self.df.copy()
        else:
            self.df_delta = self.df[self.df['Semester']
                                    != self.last_sem].copy()

    def compute_qpi(self, df):
        df['Units'] = pd.to_numeric(df['Units'], errors='coerce')
        df['Numerical Grade'] = df['Final Grade'].map(letters)
        total_units = df['Units'].sum()

        df['Weighted Grade'] = df['Units'] * df['Numerical Grade']
        weighted_grade = round(df['Weighted Grade'].sum() / total_units, 2)
        return weighted_grade

    def cumulative_qpi(self):
        return self.compute_qpi(self.df)

    def cumulative_qpi_delta(self):
        return self.compute_qpi(self.df_delta)

    def semester_qpi(self, sem):
        df = self.df
        new_df = df[df['Semester'] == sem].copy()
        return self.compute_qpi(new_df)

    def latest_qpi(self):
        return self.semester_qpi(self.last_sem)

    def latest_qpi_delta(self):
        df = self.df_delta
        previous_sem = df.iloc[-1]['Semester']
        return self.semester_qpi(previous_sem)

    def dean_list(self):
        second_honor = 3.35
        first_honor = 3.7
        if self.latest_qpi() < second_honor:
            return ' '
        if second_honor <= self.latest_qpi() < first_honor:
            return 'Second Honors'
        else:
            return 'First Honors'

    def qpi_by_semester(self):
        semesters = self.df['Semester'].unique()
        qpi_lst = []
        for s in semesters:
            qpi_lst.append(self.semester_qpi(s))
        new_df = pd.DataFrame(data={'Semester': semesters, 'QPI': qpi_lst})
        return new_df
    
    def letter_frequency(self):
        df = self.df
        return df.groupby('Final Grade')['Subject Code'].count().reset_index()
