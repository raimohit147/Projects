from django.db import models

class Sign(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    phone=models.IntegerField()
    pswd=models.CharField(max_length=10)
    cpswd=models.CharField(max_length=10)
    gender=models.CharField(max_length=7)
    
class Stafff(models.Model):
    ffname=models.CharField(max_length=20)
    llname=models.CharField(max_length=10)
    eemail=models.CharField(max_length=20 )
    pphone=models.IntegerField()
    pswrd=models.CharField(max_length=10)
    cpswrd=models.CharField(max_length=10)
    ggender=models.CharField(max_length=7)
    
class Student(models.Model):
    first=models.CharField(max_length=20)
    last=models.CharField(max_length=10)
    mail=models.CharField(max_length=20)
    mob=models.IntegerField()
    pswdd=models.CharField(max_length=10)
    cpswdd=models.CharField(max_length=10)
    genderr=models.CharField(max_length=7)
    
class Addstaff(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
    age=models.IntegerField()
    address=models.CharField(max_length=20)
    r1=models.CharField(max_length=7)
    hname=models.CharField(max_length=30)
    per=models.IntegerField()
    hsname=models.CharField(max_length=30)
    percent=models.IntegerField()
    gname=models.CharField(max_length=20)
    sname=models.CharField(max_length=10)
    percentage=models.IntegerField()
    pname=models.CharField(max_length=20)
    cname=models.CharField(max_length=10)
    per2=models.IntegerField()
    anum=models.IntegerField()
    pnum=models.IntegerField()
    email=models.CharField(max_length=20)
    
class Addstudent(models.Model):
    first=models.CharField(max_length=10)
    last=models.CharField(max_length=10)
    age=models.IntegerField()
    area=models.CharField(max_length=20)
    r1=models.CharField(max_length=7)
    hname=models.CharField(max_length=30)
    per=models.IntegerField()
    hsname=models.CharField(max_length=30)
    percent=models.IntegerField()
    anum=models.IntegerField()
    pnum=models.IntegerField()
    email=models.CharField(max_length=20)
    
class Addcourse(models.Model):
    cname=models.CharField(max_length=10)
    sname=models.CharField(max_length=10)
    
class Addsubject(models.Model):
    sub=models.CharField(max_length=10)
    cou=models.CharField(max_length=10)
    staff=models.CharField(max_length=10)
    
class Addsession(models.Model):
    start=models.DateField()
    end=models.DateField()
    
class staffleave(models.Model):
    staff1=models.CharField(max_length=30)
    leave=models.DateField()
    eleave=models.DateField()
    comment=models.TextField()
    
class Stafffeedback(models.Model):
    fd=models.CharField(max_length=10)
    msg=models.CharField(max_length=50)

class Feedback(models.Model):
    name=models.CharField(max_length=10)
    msgg=models.CharField(max_length=50)
    
class replystaff(models.Model):
    reply=models.CharField(max_length=40)
    
class Studentleave(models.Model):
    student1=models.CharField(max_length=30)
    leave=models.DateField()
    eleave=models.DateField()
    comment=models.TextField()
    
class Replystudent(models.Model):
    reply=models.CharField(max_length=40)
    
class Attend(models.Model):
    attend=models.CharField(max_length=10)
    date=models.DateField()
    day=models.CharField(max_length=10)
    p=models.CharField(max_length=10)

class Result(models.Model):
    name=models.CharField(max_length=10)
    res=models.CharField(max_length=10)

    
# Create your models here.
