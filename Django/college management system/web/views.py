from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Sign,Stafff,Student,Addstaff,Addstudent,Addcourse,Addsubject,Addsession,staffleave,Stafffeedback,Feedback,replystaff,Studentleave,Replystudent,Attend,Result
def home(req):
    return render(req,'home.html')
def about(req):
    return render(req,'about.html')
def temp(req):
    return render(req,'login.html')
def course(req):
    return render(req,'course.html')
def blog(req):
    return render(req,'blog.html')
def contact(req):
    return render(req,'contact.html')
# ------admin----
def signup(req):
    return render(req,'signup.html')
def signupsave(req):
    obj=Sign()
    obj.fname=req.POST.get('fname')
    obj.lname=req.POST.get('lname')
    obj.email=req.POST.get('email')
    obj.phone=req.POST.get('phone')
    obj.pswd=req.POST.get('pswd')
    obj.cpswd=req.POST.get('cpswd')
    obj.gender=req.POST.get('gender')
    obj.save()
    return render(req,'login.html')
    
def checklogin(req):
    fn=req.POST.get('fname')
    pas=req.POST.get('pswd')
    userResult=Sign.objects.filter(fname=fn,pswd=pas)
    if(userResult):
        listData=userResult.values()
        id=listData[0]['id']
        fname=listData[0]['fname']
        req.session['id']=id
        req.session['fname']=fname
        return render(req,'check.html')
    else:
        return render(req,'login.html',{'result':'invalid'})
def logout(req):
    return render(req,'home.html')

# -------staff----
def staff(req):
    return render(req,'staffsignup.html')
def staffsave(req):
    obj=Stafff()
    obj.ffname=req.POST.get('ffname')
    obj.llname=req.POST.get('llname')
    obj.eemail=req.POST.get('eemail')
    obj.pphone=req.POST.get('pphone')
    obj.pswrd=req.POST.get('pswrd')
    obj.cpswrd=req.POST.get('cpswrd')
    obj.ggender=req.POST.get('ggender')
    obj.save()
    return render(req,'stafflogin.html')
def staffchecklogin(req):
    fnt=req.POST.get('ffname')
    passs=req.POST.get('pswrd')
    userResult=Stafff.objects.filter(ffname=fnt,pswrd=passs)
    if(userResult):
        listData=userResult.values()
        id=listData[0]['id']
        ffname=listData[0]['ffname']
        req.session['id']=id
        req.session['ffname']=ffname
        return render(req,'staffdashboard.html')
    else:
        return render(req,'stafflogin.html')
def logout(req):
    return render(req,'home.html')

# -----student----
def students(req):
    return render(req,'studentsignup.html')
def studentsave(req):
    obj=Student()
    obj.first=req.POST.get('first')
    obj.last=req.POST.get('last')
    obj.mail=req.POST.get('mail')
    obj.mob=req.POST.get('mob')
    obj.pswdd=req.POST.get('pswdd')
    obj.cpswdd=req.POST.get('cpswdd')
    obj.genderr=req.POST.get('genderr')
    obj.save()
    return render(req,'studentlogin.html')
def studentchecklogin(req):
    first=req.POST.get('first')
    pswdd=req.POST.get('pswdd')
    userResult=Student.objects.filter(first=first,pswdd=pswdd)
    if(userResult):
        listData=userResult.values()
        id=listData[0]['id']
        first=listData[0]['first']
        req.session['id']=id
        req.session['first']=first
        return render(req,'studentdashboard.html')
    else:
        return render(req,'studentlogin.html')
def logout(req):
    return render(req,'home.html')

# ------add staff----
def addstaff(req):
    return render(req,'addstaff.html') 
def addstaffsave(req):
    obj=Addstaff()
    obj.fname=req.POST.get('fname')
    obj.lname=req.POST.get('lname')
    obj.age=req.POST.get('age')
    obj.address=req.POST.get('address')
    obj.r1=req.POST.get('r1')
    obj.hname=req.POST.get('hname')
    obj.per=req.POST.get('per')
    obj.hsname=req.POST.get('hsname')
    obj.percent=req.POST.get('percent')
    obj.gname=req.POST.get('gname')
    obj.sname=req.POST.get('sname')
    obj.percentage=req.POST.get('percentage')
    obj.pname=req.POST.get('pname')
    obj.cname=req.POST.get('cname')
    obj.per2=req.POST.get('per2')
    obj.anum=req.POST.get('anum')
    obj.pnum=req.POST.get('pnum')
    obj.email=req.POST.get('email')
    obj.save()
    return render(req,'check.html')

def managestaff(req):
    result=Addstaff.objects.all()
    return render(req,'manage.html',{'result':result})
def deletestaff(req):
    id=req.GET.get('x')
    result=Addstaff.objects.get(id=id)
    result.delete()
    return redirect('/managestaff')

# ----addstudent----
def addstudent(req):
    return render(req,'addstudent.html') 
def addstudentsave(req):
    obj=Addstudent()
    obj.first=req.POST.get('first')
    obj.last=req.POST.get('last')
    obj.age=req.POST.get('age')
    obj.area=req.POST.get('area')
    obj.r1=req.POST.get('r1')
    obj.hname=req.POST.get('hname')
    obj.per=req.POST.get('per')
    obj.hsname=req.POST.get('hsname')
    obj.percent=req.POST.get('percent')
    obj.anum=req.POST.get('anum')
    obj.pnum=req.POST.get('pnum')
    obj.email=req.POST.get('email')
    obj.save()
    return render(req,'check.html')

def managestudent(req):
    result=Addstudent.objects.all()
    return render(req,'managestudent.html',{'result':result})
def deletestudent(req):
    id=req.GET.get('x')
    result=Addstudent.objects.get(id=id)
    result.delete()
    return redirect('/managestudent')

# ------add course---
def addcourse(req):
    return render(req,'addcourse.html') 
def addcoursesave(req):
    obj=Addcourse()
    obj.cname=req.POST.get('cname')
    obj.sname=req.POST.get('sname')
    obj.save()
    return render(req,'check.html')

def managecourse(req):
    result=Addcourse.objects.all()
    return render(req,'managecourse.html',{'result':result})
def deletecourse(req):
    id=req.GET.get('x')
    result=Addcourse.objects.get(id=id)
    result.delete()
    return redirect('/managecourse')

# -----add subject---
def addsubject(req):
    return render(req,'addsubject.html') 
def addsubjectsave(req):
    obj=Addsubject()
    obj.sub=req.POST.get('sub')
    obj.cou=req.POST.get('cou')
    obj.staff=req.POST.get('staff')
    obj.save()
    return render(req,'check.html')

def managesubject(req):
    result=Addsubject.objects.all()
    return render(req,'managesubject.html',{'result':result})
def deletesubject(req):
    id=req.GET.get('x')
    result=Addstaff.objects.get(id=id)
    result.delete()
    return redirect('/managesubject')

# ----add session---
def addsession(req):
    return render(req,'addsession.html') 
def addsessionsave(req):
    obj=Addsession()
    obj.start=req.POST.get('start')
    obj.end=req.POST.get('end')
    obj.save()
    return render(req,'check.html')

def managesession(req):
    result=Addsession.objects.all()
    return render(req,'managesession.html',{'result':result})
def deletesession(req):
    id=req.GET.get('x')
    result=Addstaff.objects.get(id=id)
    result.delete()
    return redirect('/managesession')

# ------staffleave----
def stafleave(req):
    return render(req,'staffleave.html')
def staffleavesave(req):
    obj=staffleave()
    obj.staff1=req.POST.get('staff1')
    obj.leave=req.POST.get('leave')
    obj.eleave=req.POST.get('eleave')
    obj.comment=req.POST.get('comment')
    obj.save()
    return render(req,'staffdashboard.html')
def managestaffleave(req):
    result=staffleave.objects.all()
    return render(req,'managestaffleave.html',{'result':result})


# ------stafffeedback---
def stafffeedback(req):
    return render(req,"stafffeedback.html")
def stafffeedbacksave(req):
    obj=Stafffeedback()
    obj.fd=req.POST.get('fd')
    obj.msg=req.POST.get('msg')
    obj.save()
    return render(req,'staffdashboard.html') 
def managestafffeedback(req):
    result=Stafffeedback.objects.all()
    return render(req,'managestafffeedback.html',{'result':result})
def deletestafffeedback(req):
    id=req.GET.get('x')
    result=Stafffeedback.objects.get(id=id)
    result.delete()
    return redirect('/managestafffeedback')

# ------Studentfeedback----
def studentfeedback(req):
    return render(req,"studentfeedback.html")
def studentfeedbacksave(req):
    obj=Feedback()
    obj.name=req.POST.get('name')
    obj.msgg=req.POST.get('msgg')
    obj.save()
    return render(req,'studentdashboard.html') 
def managestudentfeedback(req):
    result=Feedback.objects.all()
    return render(req,'managestudentfeedback.html',{'result':result})
def deletestudentfeedback(req):
    id=req.GET.get('x')
    result=Feedback.objects.get(id=id)
    result.delete()
    return redirect('/managestudentfeedback')

# -----staffreply----
def staffreply(req):
    return render(req,'staffreply.html')
def staffreplysave(req):
    obj=replystaff()
    obj.reply=req.POST.get('reply')
    obj.save()
    return render(req,'check.html')
def viewstaffleave(req):
    result=replystaff.objects.all()
    return render(req,'reply.html',{'result':result})
def deletestaffleave(req):
    id=req.GET.get('x')
    result=replystaff.objects.get(id=id)
    result.delete()
    return redirect('/viewstaffleave')

# ------studentleave-----
def studentleave(req):
    return render(req,'studentleave.html')
def studentleavesave(req):
    obj=Studentleave()
    obj.student1=req.POST.get('student1')
    obj.leave=req.POST.get('leave')
    obj.eleave=req.POST.get('eleave')
    obj.comment=req.POST.get('comment')
    obj.save()
    return render(req,'studentdashboard.html')
def managestudentleave(req):
    result=Studentleave.objects.all()
    return render(req,'managestudentleave.html',{'result':result})

# -----studentreply----
def studentreply(req):
    return render(req,'studentreply.html')
def studentreplysave(req):
    obj=Replystudent()
    obj.reply=req.POST.get('reply')
    obj.save()
    return render(req,'check.html')
def viewstudentleave(req):
    result=Replystudent.objects.all()
    return render(req,'replyystd.html',{'result':result})
def deletestudentleave(req):
    id=req.GET.get('x')
    result=Replystudent.objects.get(id=id)
    result.delete()
    return redirect('/viewstudentleave')

# ----Attend---
def attend(req):
    return render(req,"attend.html")
def attendsave(req):
    obj=Attend()
    obj.attend=req.POST.get('attend')
    obj.date=req.POST.get('date')
    obj.day=req.POST.get('day')
    obj.p=req.POST.get('p')
    obj.save()
    return render(req,'attend.html')
def manageattend(req):
    result=Attend.objects.all()
    return render(req,'manageattend.html',{'result':result})
def deleteattend(req):
    id=req.GET.get('x')
    result=Attend.objects.get(id=id)
    result.delete()
    return redirect('/manageattend')
def back(req):
    return render(req,'staffdashboard.html')

# -----result----
def result(req):
    return render(req,"addresult.html")
def saveresult(req):
    obj=Result()
    obj.name=req.POST.get('name')
    obj.res=req.POST.get('res')
    obj.save()
    return render(req,'addresult.html')
def manageresult(req):
    result=Result.objects.all()
    return render(req,'manageresult.html',{'result':result})
# Create your views here.
