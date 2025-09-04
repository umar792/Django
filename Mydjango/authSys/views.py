from django.shortcuts import render




# signup route
def signUp(request):
    return render(request,"signup.html")