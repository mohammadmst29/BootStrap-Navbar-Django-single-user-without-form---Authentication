
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User


def homepage(request):

    return render (request, 'homepage.html')

def signuppage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'signuppage.html', {'error': 'Passwords do not match'})
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        return redirect('loginpage')
    return render(request, 'signuppage.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')  
        else:
            return render(request, 'loginpage.html', {'error': 'Invalid username or password'})
    return render(request, 'loginpage.html')

def logoutuser(request):
    logout(request)
    return redirect('loginpage')