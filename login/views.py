from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            if remember_me == 'on':
                request.session.set_expiry(2592000)
                request.session['remember_me'] = True
            else:
                request.session.pop('remember_me', None)
            return redirect('/')
        else:
            messages.success(request, ("There Was An Error Logging In, Please Try Again!"))
            return redirect('/login')
    else:
        remember_me = request.session.get('remember_me', False)
        if remember_me:
            username = request.session.get('username', '')
            password = request.session.get('password', '')
            return render(request, 'pages/login.html', {'username': username, 'password': password})
        else:
            return render(request, 'pages/login.html', {})