from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout , authenticate , login
from . models import product

# Create your views here.

def home(request):
    product_data = product.objects.all()[:4]
    return render(request , 'index.html' , {'Product' : product_data })

def about(request):
    return render(request,'about.html')

def shop(request):
    return render(request,'shop.html')

def furniture(request):
    return render(request ,'furniture.html')

def contact(request):
    return render(request ,'contact.html')

def allproduct(request):
    product_data = product.objects.all()
    return render(request , 'allproduct.html' , {'Product' : product_data })

def auth(request):
    return render(request , 'auth.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']

        first_name = name.split(' ')[0]
        last_name = name.split(' ')[1]

        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = email , 
            password = password 
            )
        user.save()
        return redirect('/')

def signin(request):
    username = request.POST['email']
    password = request.POST['password']
    user = authenticate(username = username , password = password)
    if user is not None:
        login(request,user)
        return redirect('/')
    else:
        return redirect('/auth')
    
def log(request):
    logout(request)
    return redirect('/')

