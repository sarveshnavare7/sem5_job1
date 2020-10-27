from django.shortcuts import render
from JobPortal1.models import sqlserverconn,applicant
import pyodbc

def connsql(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-QLPV3KL;'
                        'Database=dbisLab;'
                        'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("select * from Company")
    result=cursor.fetchall()
    #return render(request,'job_portal-master/registerasseeker.html')
    return render(request,'index.html',{'sqlserverconn':result})

def seekerreg(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=DESKTOP-QLPV3KL;'
                        'Database=dbisLab;'
                        'Trusted_Connection=yes;')
    if request.method=='POST':
        if request.POST.get('jaadharnumber') and request.POST.get('jfname') and request.POST.get('jlname') and request.POST.get('jcity') and  request.POST.get('jstate') and  request.POST.get('jemail'):
            iv=applicant()
            iv.jaadharnumber=request.POST.get('jaadharnumber')
            iv.jfname=request.POST.get('jfname')
            iv.jlname=request.POST.get('jlname')
            iv.jcity=request.POST.get('jcity')
            iv.jstate=request.POST.get('jstate')
            iv.jemail=request.POST.get('jemail')
            iv.jcontactNumber=request.POST.get('jcontactNumber')
            iv.jage=30
            cursor=conn.cursor()
            cursor.execute("insert into Applicant values ('"+iv.jaadharnumber+"','"+iv.jfname+"','"+iv.jlname+"','"+iv.jcity+"','"+iv.jstate+"','"+iv.jemail+"','"+iv.jcontactNumber+"','"+iv.jage+"')")
            cursor.commit()
            return render(request,'job_portal-master/registerasseeker.html')
    else:
            return render(request,'job_portal-master/registerasseeker.html')    
        
    