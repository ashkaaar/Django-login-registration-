from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            login(request, user)
            # Implement email confirmation logic here
            return redirect('home')  # Redirect to your home page
    else:
        form = RegistrationForm()
    return render(request, 'authentication/register.html', {'form': form})