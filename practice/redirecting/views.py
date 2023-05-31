from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.

def redirecting(request):
    print(request.body)
    if request.method == "POST":
        fm = StudentRegistration(request.POST,)
        if fm.is_valid(): 
            print("Name: {}".format(fm.cleaned_data["Name"]))
            print("Email: {}".format(fm.cleaned_data["Email"]))
            name = fm.cleaned_data["Name"]
            email = fm.cleaned_data["Email"]
            password = fm.cleaned_data["Password"]
            # fm = StudentRegistration()

            # *Using render function to redirect on next page does not change the URL after successfully redirecting to next page 
            # *but if we do this using HttpResponseRedirect() function than our URL will also change
            # return render(request, "redirecting/success.html", {"name":name})

            # Basically HttpResponseRedirect() function redirects us on different view function 
            # Trailing slash is mandatory
            return HttpResponseRedirect("/redi/success")


        # print(fm)

    else:
        fm = StudentRegistration(initial={"Name":''})
        print(fm)
        # print("This is Get request")
    # fm = StudentRegistration()
    # return render(request,'app1/userregistration.html', {"form":fm})
    return render(request, "redirecting/userregistration6.html", {"form":fm})


def success(request):
    return render(request, "redirecting/success.html")