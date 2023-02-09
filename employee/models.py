from django.db import models

# Create your models here.

class Employee(models.Model):
    emp_no=models.IntegerField('employee number', primary_key=True)
    birth_date=models.DateField('birthday')
    first_name=models.CharField('first name', max_length=100)
    last_name=models.CharField('last name', max_length=100)
    gender=models.CharField('gender',max_length=10)
    hire_date=models.DateField('hire date')


    class Meta:
        db_table='employees'

    

    def __str__(self):
        return "{} {}".format(self.first_name,self.last_name)
