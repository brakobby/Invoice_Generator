# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import InvGen  # Your custom user model


# ==================== REGISTER ====================
def Registration(request):
    if request.method == "POST":
        # Get form data
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip().lower()
        company_name = request.POST.get('company_name', '').strip()
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')

        # 1. Check if all fields are filled
        if not all([first_name, last_name, email, company_name, password, conf_password]):
            messages.error(request, "Please fill in all fields.")
            return redirect('register')

        # 2. Check password match
        if password != conf_password:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # 3. Check if email already exists
        if InvGen.objects.filter(email=email).exists():
            messages.error(request, "An account with this email already exists.")
            return redirect('register')

        # 4. Save user
        try:
            hashed_password = make_password(password)
            user = InvGen.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                company_name=company_name,
                password=hashed_password
            )
            user.save()
            messages.success(request, f"Welcome {first_name}! Your account has been created.")
            return redirect('login')

        except Exception as e:
            messages.error(request, "Something went wrong. Please try again.")
            return redirect('register')

    # GET request
    return render(request, 'users/register.html')


# ==================== LOGIN ====================
def Login(request):
    if request.method == "POST":
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password')

        # Check if fields are filled
        if not email or not password:
            messages.error(request, "Please enter both email and password.")
            return redirect('login')

        try:
            # Fetch user by email
            user = InvGen.objects.get(email=email)

            # Verify password
            if check_password(password, user.password):
                # SUCCESS → Create session manually
                request.session['user_id'] = user.id
                request.session['user_name'] =user.first_name
                request.session['last_name'] = user.last_name
                request.session['company'] = user.company_name

                messages.success(request, f"Welcome back, {user.first_name}!")
                return redirect('dashboard')  # Change to your home page

            else:
                messages.error(request, "Incorrect password.")

        except InvGen.DoesNotExist:
            messages.error(request, "No account found with this email.")

        return redirect('login')

    # GET request
    return render(request, 'users/login.html')