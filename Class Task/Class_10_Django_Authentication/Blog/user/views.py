from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user data
            return reverse_lazy('login')  # Redirect to the login page after registration
        return render(request, 'register.html', {'form': form})



class CustomLoginView(View):
    def get(self, request):
        # Display the login form
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # If the user exists and the credentials are correct, log them in
            login(request, user)
            return redirect('home')  # Redirect to the homepage or a dashboard
        else:
            # Check if the user exists to differentiate between incorrect username or password
            from django.contrib.auth.models import User
            if User.objects.filter(username=username).exists():
                # If the username exists but the password is wrong
                messages.error(request, 'Incorrect password. Please try again.')
            else:
                # If the username doesn't exist
                messages.error(request, 'User not found. Please register first.')
                
            return redirect('login')