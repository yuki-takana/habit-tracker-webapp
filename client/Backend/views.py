from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from datetime import date, timedelta
from Backend.models import Habit, Completion
from django.contrib import messages


# Helper function to calculate the current streak for a habit
def calculate_streak(habit):
    today = date.today()
    streak = 0
    current_day = today

    while True:
        exists = Completion.objects.filter(habit=habit, date=current_day).exists()
        if exists:
            streak += 1
            current_day -= timedelta(days=1)
        else:
            break
    return streak


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid username or password.'
    return render(request, 'login.html', {'error': error})

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    habits = request.user.habit_set.all()
    habit_data = []
    for habit in habits:
        habit_data.append({
            'habit': habit,
            'streak': calculate_streak(habit),
        })
    return render(request, 'dashboard.html', {'habit_data': habit_data})

@login_required(login_url='login')
def manage_habits(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        frequency = request.POST.get('frequency')

        if not name:
            messages.error(request, "Habit name cannot be empty.")
            return redirect('manage_habits')

        # Convert frequency to integer and handle invalid input
        try:
            frequency = int(frequency)
            if frequency < 1:
                raise ValueError
        except (ValueError, TypeError):
            messages.error(request, "Frequency must be a positive integer.")
            return redirect('manage_habits')

        # Create habit
        Habit.objects.create(
            user=request.user,
            name=name,
            frequency=frequency
            )
        messages.success(request, "Habit added successfully!")
        return redirect('manage_habits')

    # GET request — show all habits
    habits = request.user.habit_set.all()
    return render(request, 'manage_habits.html', {'habits': habits})
