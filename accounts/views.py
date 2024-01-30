from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')


def contactus(request):
    if request.method=='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']

        if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already taken.. try other email')
                return redirect('contactus')
        
        elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already taken.. try other username')
                return redirect('contactus')
        else:      
                user = User.objects.create_user(email = email, first_name = first_name,last_name = last_name,username = username )
                user.save();
                messages.info(request, 'Info Sent Successfully')
                
                return redirect('contactus')

        
    else:    
       return render(request, 'contactus.html')


# def home(request):
#     return render(request, 'index.html')
