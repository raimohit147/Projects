"""
URL configuration for cms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views as v1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v1.home),
    path('about',v1.about),
    path('course',v1.course),
    path('temp',v1.temp),
    path('checklogin',v1.checklogin),
    path('blog',v1.blog),
    path('contact',v1.contact),
    path('signup',v1.signup),
    path('signupsave',v1.signupsave),
    path('logout',v1.logout),
    path('staffsave',v1.staffsave),
    path('staff',v1.staff),
    path('students',v1.students),
    path('studentsave',v1.studentsave),
    path('staffchecklogin',v1.staffchecklogin),
    path('studentchecklogin',v1.studentchecklogin),
    path('addstaff',v1.addstaff),
    path('addstaffsave',v1.addstaffsave),
    path('managestaff',v1.managestaff),
    path('deletestaff',v1.deletestaff),
    path('addstudent',v1.addstudent),
    path('addstudentsave',v1.addstudentsave),
    path('managestudent',v1.managestudent),
    path('deletestudent',v1.deletestudent),
    path('addcourse',v1.addcourse),
    path('addcoursesave',v1.addcoursesave),
    path('managecourse',v1.managecourse),
    path('deletecourse',v1.deletecourse),
    path('addsubject',v1.addsubject),
    path('addsubjectsave',v1.addsubjectsave),
    path('managesubject',v1.managesubject),
    path('deletesubject',v1.deletesubject),
    path('addsession',v1.addsession),
    path('addsessionsave',v1.addsessionsave),
    path('managesession',v1.managesession),
    path('deletesession',v1.deletesession),
    path('stafleave',v1.stafleave),
    path('staffleavesave',v1.staffleavesave),
    path('managestaffleave',v1.managestaffleave),
    path('viewstaffleave',v1.viewstaffleave),
    path('stafffeedback',v1.stafffeedback),
    path('stafffeedbacksave',v1.stafffeedbacksave),
    path('managestafffeedback',v1.managestafffeedback),
    path('deletestafffeedback',v1.deletestafffeedback),
    path('studentfeedback',v1.studentfeedback),
    path('studentfeedbacksave',v1.studentfeedbacksave),
    path('managestudentfeedback',v1.managestudentfeedback),
    path('deletestudentfeedback',v1.deletestudentfeedback),
    path('staffreply',v1.staffreply),
    path('staffreplysave',v1.staffreplysave),
    path('deletestaffleave',v1.deletestaffleave),
    path('studentleave',v1.studentleave),
    path('studentleavesave',v1.studentleavesave),
    path('managestudentleave',v1.managestudentleave),
    path('studentreply',v1.studentreply),
    path('studentreplysave',v1.studentreplysave),
    path('viewstudentleave',v1.viewstudentleave),
    path('deletestudentleave',v1.deletestudentleave),
    path('attend',v1.attend),
    path('attendsave',v1.attendsave),
    path('manageattend',v1.manageattend),
    path('deleteattend',v1.deleteattend),
    path('back',v1.back),
    path('result',v1.result),
    path('saveresult',v1.saveresult),
    path('manageresult',v1.manageresult),
]
