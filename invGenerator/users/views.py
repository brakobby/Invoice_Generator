from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InvGen
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

    # Register

def Registration(request):
    if request.method == "POST":
        email = request.POST.get['email']
        fullname = request.POST.get['fullname']
        company_name = request.POST.get['company_name']
        password = request.POST.get['password']
        conf_password = request.POST.get['conf_password']

        # checking if password is = to conf_password

        if password != conf_password:
            messages.error(request,"Password do not match")
            return redirect("?")

        # checking if you have filled all fields

        if not (email and fullname and company_name and password and conf_password):
            messages.error(request,"Please fill all fields before submission")

        hashed_password = make_password(password)

        # saving the fields

        UserAccount = InvGen.objects.create(
            email = email,
            fullname = fullname,
            company_name = company_name,
            password = hashed_password,
        )

        UserAccount.save()
        messages.success(request, "Account has been created successfully")
        return redirect('login')

    return render(request, 'users/register.html')

# Login

def Login(request):
    if request.method == 'POST':
        email = request.POST.get['email']
        password = request.POST.get['password']

        try:
            userAccount = InvGen.objects.create(email = email)

            # Making sure the password matches

            if check_password(password, userAccount.password):
                messages.success(request,f"Welcome {userAccount.fullname}")
                return render(request, 'users/login.html', {'user' : userAccount})

            else:
                messages.error(request, "Invalid password")
                return redirect('Login')

        # What will happen when you haven't even registered

        except Registration.DoesNotExist:
            messages.error(request, 'Invalid username or password')

            return redirect('Login')
    return render(request, 'users/login.html')