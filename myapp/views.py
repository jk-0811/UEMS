from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .models import Event, EventRegistration
from .forms import ContactForm, EventRegistrationForm
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()



# Home Page
def home(request):
    return render(request, 'home.html')

# About Page
def about(request):
    return render(request, 'about.html')

# Events Page (Show all events)
def events(request):
    all_events = Event.objects.all()
    return render(request, 'events.html', {'events': all_events})

# Sponsors Page
def sponsors(request):
    return render(request, 'sponsors.html')

# Specific Event Pages
def conference(request):
    return render(request, 'conference.html')

def ai_workshop(request):
    return render(request, 'ai.html')

def chatbot_workshop(request):
    return render(request, 'chatbot.html')

# Contact Page (Form Submission)
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                "New Contact Form Submission",
                f"Message from {form.cleaned_data['name']}:\n{form.cleaned_data['message']}",
                form.cleaned_data['email'],
                ['admin@example.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent!")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Event Registration Page
def register_event(request, event_id):
    return redirect('dashboard')  # Redirects to the dashboard immediately

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()  # ✅ Use your custom user model

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

@csrf_exempt
def submit_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password', '').strip()
        confirm_password = request.POST.get('confirm_password', '').strip()
        event_name = request.POST.get('event_name', '')

        # Validation
        if not name or not email or not password or not confirm_password:
            return JsonResponse({'success': False, 'error': 'Please fill all fields.'})

        if password != confirm_password:
            return JsonResponse({'success': False, 'error': 'Passwords do not match.'})

        if User.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'error': 'An account with this email already exists.'})

        # Create user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        user.full_name = name  # Make sure your User model supports this field
        user.phone = phone     # Likewise, this field must exist or be handled via a profile model
        user.save()

        # Success response
        return JsonResponse({'success': True})

    # Not a POST request
    return JsonResponse({'success': False, 'error': 'Invalid request method.'})




# User Dashboard (Requires Login)
@login_required
def dashboard_view(request):
    if request.user.is_staff:
        return redirect('admin_dashboard')
    else:
        return redirect('user_dashboard')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')

@login_required
def user_dashboard(request):
    return render(request, 'user_dashboard.html')

def registration(request):
    return render(request, "registration.html")

def dashboard(request):
    return render(request, 'dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # or wherever you want to go after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

from django.contrib.auth import get_user_model
CustomUser = get_user_model()
