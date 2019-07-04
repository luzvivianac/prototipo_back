from django.db import models
from datetime import date

# Create your models here.
class Institution(models.Model):
    country = models.CharField(max_length = 50, blank = True)
    long_name = models.CharField(max_length = 255)
    short_name = models.CharField(max_length = 50)
    formal_inst = models.BooleanField(default = True)

class Id_Type(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(blank = True)

class Tutor(models.Model):
    name = models.CharField(max_length = 150)
    id_number = models.CharField(max_length = 20)
    email = models.EmailField(null = True, blank = True)
    id_type = models.ForeignKey('Id_Type', on_delete = models.SET_NULL, null = True, blank = True)

class TutorXInstitution(models.Model):
    tutor = models.ForeignKey('Tutor', on_delete = models.CASCADE)
    institution = models.ForeignKey('Institution', on_delete = models.CASCADE)

class Program(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    institution = models.ForeignKey('Institution', on_delete = models.CASCADE)

class Grade_Area(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    program = models.ForeignKey('Program', on_delete = models.CASCADE)

class Subject(models.Model):
    name = models.CharField(max_length = 100)
    grade_area = models.ForeignKey('Grade_Area', on_delete = models.CASCADE)

class Period(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(blank = True)
    initial_date = models.DateField(default = date.today)
    final_date = models.DateField()
    program = models.ForeignKey('Program', on_delete = models.CASCADE)

class Group(models.Model):
    name = models.CharField(max_length = 100)
    period = models.ForeignKey('Period', on_delete = models.SET_NULL, null = True, blank = True)
    tutor = models.ForeignKey('Tutor', on_delete = models.SET_NULL, null = True, blank = True)
    grade_area = models.ForeignKey('Grade_Area', on_delete = models.SET_NULL, null = True, blank = True)

class Student(models.Model):
    name = models.CharField(max_length = 100)
    id_number = models.CharField(max_length = 20)
    birth_date = models.DateField()
    address = models.CharField(max_length = 200, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    phone = models.CharField(max_length = 20)
    id_type = models.ForeignKey('Id_Type', on_delete = models.SET_NULL, null = True, blank = True)

class StudentXInstitution(models.Model):
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    institution = models.ForeignKey('Institution', on_delete = models.CASCADE)

class StudentXGroup(models.Model):
    row_number = models.PositiveSmallIntegerField(default = 0)
    column_number = models.PositiveSmallIntegerField(default = 0)
    studentxinstitution = models.ForeignKey('StudentXInstitution', on_delete = models.CASCADE)
    group = models.ForeignKey('Group', on_delete = models.CASCADE)

class Attendace(models.Model):
    date = models.DateField(default = date.today)
    excuse = models.TextField(blank = True)
    # 0 In class. 1. Not in class 
    att_type = models.PositiveSmallIntegerField(default = 0)
    studentxgroup = models.ForeignKey('StudentXGroup', on_delete = models.CASCADE)

class Diagnostic(models.Model):
    short_name = models.CharField(max_length = 50)
    long_name = models.CharField(max_length = 255)
    description = models.TextField(blank = True)

class StudentXDiagnostic(models.Model):
    date = models.DateField(default = date.today)
    observation = models.TextField(blank = True)
    presumptive = models.BooleanField(default = False)
    student = models.ForeignKey('Student', on_delete = models.CASCADE)
    diagnostic = models.ForeignKey('Diagnostic', on_delete = models.CASCADE)

class Category(models.Model):
    # 0 Comportamental. 1. Cognitiva 
    cat_type = models.PositiveSmallIntegerField(default = 0)
    description = models.TextField(blank = True)
    name = models.CharField(max_length = 100)
    icon = models.CharField(max_length = 255, blank = True, null = True)
    init_date = models.DateField(default = date.today)
    final_date = models.DateField(null = True, blank = True)
    parent_id = models.ForeignKey('self', on_delete = models.SET_NULL, null = True, blank = True)
    grade_area = models.ForeignKey('Grade_Area', on_delete = models.SET_NULL, null = True, blank = True)

class Monitoring(models.Model):
    date = models.DateField(default = date.today)
    repetitions = models.PositiveIntegerField(default = 0)
    observation = models.TextField(blank = True)
    category = models.ForeignKey('Category', on_delete = models.CASCADE)
    studentxgroup = models.ForeignKey('StudentXGroup', on_delete = models.CASCADE)