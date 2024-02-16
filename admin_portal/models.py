from django.db import models
import uuid

class Department(models.Model):
    d_id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    dept_name=models.CharField(max_length=200)

    def __str__(self):
        return self.dept_name
    
class Elective(models.Model):
    e_id=models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True,editable=False)
    elective_name=models.CharField(max_length=200)

    def __str__(self):
        return self.elective_name

class StudentInfo(models.Model):
    s_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    jntu_no = models.CharField(max_length=20)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True)
    section = models.CharField(max_length=10)
    email = models.EmailField()
    curr_sem = models.IntegerField()

    def __str__(self):
        return self.name
    

class ElectivesInfo(models.Model):
    course_code = models.CharField(max_length=20)
    elective_name = models.OneToOneField(Elective,on_delete=models.SET_NULL,blank=True,null=True)
    offering_department = models.OneToOneField(Department,on_delete=models.SET_NULL,blank=True,null=True)
    offering_strength = models.IntegerField()
    not_allowed_students = models.ManyToManyField(StudentInfo, blank=True)

    def __str__(self):
        return self.elective_name.elective_name
    
class ResultsElectiveWise(models.Model):
    id= models.UUIDField(primary_key=True)
    elective_name = models.OneToOneField(Elective,on_delete=models.SET_NULL,blank=True,null=True)
    stu_name = models.ForeignKey('StudentInfo', on_delete=models.CASCADE)
    department = models.OneToOneField(Department,on_delete=models.SET_NULL,blank=True,null=True)

    def __str__(self):
        return self.stu_name


class RegistrationTime(models.Model):
    start_date = models.DateField(null=True,blank=True)
    start_time = models.TimeField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    end_time = models.TimeField(null=True,blank=True)
