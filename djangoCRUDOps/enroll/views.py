from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.
def add_show(request):
    if request.method == "POST": 
        fm = StudentRegistration(request.POST)
        
        if fm.is_valid(): 
            nm = fm.cleaned_data.get("name")
            em = fm.cleaned_data.get("email")
            pw = fm.cleaned_data["password"]

            print(nm, em, pw)

            fm.save()

        # Showing blank form after User submits the data: 
            fm = StudentRegistration()
    else: 
        fm = StudentRegistration()
    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form':fm, 'stu':stud})



# We have two ways to save data into DB, 
# 1- we can save data through model forms .save() function 
# 2- we can save data through Model Object 

# Above Code explains the 1st approach and below code is for 2nd approach 


# def add_show(request):
#     if request.method == "POST": 
#         fm = StudentRegistration(request.POST)
        
#         if fm.is_valid(): 
#             nm = fm.cleaned_data.get("name")
#             em = fm.cleaned_data.get("email")
#             pw = fm.cleaned_data["password"]

#             print(nm, em, pw)

#             # fm.save()
#             obj = User(name= nm, email = em, password=pw)
#             obj.save()

#     else: 
#         fm = StudentRegistration()

#     return render(request, 'enroll/addandshow.html', {'form':fm})




# Delete Function


def delete_data(request,id):
    if request.method == "POST": 
        record = User.objects.get(pk=id)
        record.delete()

    return HttpResponseRedirect('/')