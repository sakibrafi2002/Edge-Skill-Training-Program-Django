from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.urls import reverse_lazy
from django.contrib import messages

# restframework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user data
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page after registration
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
            return redirect('book_list')  # Redirect to the book list
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
        
        
def CustomLogout(request):
    if request.user.is_authenticated:
        logout(request)
    context = {'x':2}
    return render(request,'login.html',context)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)