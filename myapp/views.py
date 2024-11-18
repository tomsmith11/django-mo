from django.shortcuts import render
from django.http import HttpResponse
from .models import User

def home(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Create user
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()

        return HttpResponse('User created successfully')
    return render(request, 'home.html')