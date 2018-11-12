from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    return render(request, 'personal/home.html')
# Create your views here.

def contact(request):
	return render(request, 'personal/basic.html', 
	{'content':{'If you would like to contact me, please contact me', 'jan.klenner@gmx.de'}})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register/signup.html', {'form': form})

# Create your views here.