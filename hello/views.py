from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def home(request):
    return render(request,"home.html")


def display(request):
    firstname = request.GET['firstname']
    lastname = request.GET['lastname']  
    dob = request.GET['dob']
    gender = request.GET['gender']
    nationality = request.GET['nationality']
    city = request.GET['city']
    state = request.GET['state']
    pincode = request.GET['pincode']
    qualification = request.GET['qualification']
    salary =int(request.GET['salary'])
    pannumber = request.GET['pannumber']
 

    if len(firstname) != 0 or len(firstname) >2:
        if len(lastname) != 0 or len(lastname) >2:
            if datetime.datetime.strptime(dob, '%Y-%m-%d'):
                if gender == 'male' or gender == 'female':
                    if len(nationality) >= 3:
                        if len(city) >= 3:
                            if len(state) >= 3:
                                if len(pincode) == 6:
                                    if len(qualification)>2:
                                        if salary >10000:
                                            if len(pannumber) == 10:
                                                return render(request,"result.html",{'operation': 'success'})
                                            else:
                                                return render(request,'result.html',{'operation':'reject'})
    


