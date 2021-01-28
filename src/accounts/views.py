from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
def login(request):
    #if user is authenticated already and try to use login url, this will redirect to another page
    if request.user.is_authenticated :
        return redirect('home')

    #login authentication
    if request.method == 'POST':
        #login user
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # messages.success(request, 'You are now logged out')
        return render(request,'accounts/logout.html')   