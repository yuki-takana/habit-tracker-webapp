from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import date, timedelta
from Backend.models import Habit, Completion

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