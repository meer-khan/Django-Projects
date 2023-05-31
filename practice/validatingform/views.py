from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def validatingform(request):
    print(request.body)
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid(): 
            print("Name: {}".format(fm.cleaned_data["Name"]))
            print("Email: {}".format(fm.cleaned_data["Email"]))
            fm = StudentRegistration()

        # print(fm)

    else:
        fm = StudentRegistration()
        print(fm)
        # print("This is Get request")
    # fm = StudentRegistration()
    # return render(request,'app1/userregistration.html', {"form":fm})
    return render(request, "validatingform/userregistration5.html", {"form":fm})