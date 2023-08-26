from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecord
from .models import Record

# Create your views here.


def home(request):

    
    records = Record.objects.all()

    

    # check to see if they are logging in
    if request.method == 'POST':
        username = request.POST['Username']
        password = request.POST['password']

        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are logged in')
            return redirect('home')
        else:
            messages.success(
                request, 'There was an error logging in. Please try again')
            return redirect('home')

    # if the request is not a post then it's a get method so we show them the home page
    else:
        return render(request, 'home.html', {'records': records})


# login


#def login_user(request):
    #pass


def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect('home')


def signup(request):

    #if request is a post, send all data to signupform and do something
    if request.method == 'POST':
        #pass request data into signup form created 
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            #authenticate and log them in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username= username, password = password)

            login(request, user)
            messages.success(request, 'You have signed up successfully')
            return redirect('home')
    else:
        #instance of form which we pass as a context 
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    return render(request, 'signup.html', {'form': form})


def new_record(request): 
    if request.user.is_authenticated:
       
      if request.method == 'POST':
       form =AddRecord(request.POST)
       if form.is_valid:
           
           form.save()
           messages.success(request, "Entry added successfully")
           return redirect('home')
      else:
        
         news = AddRecord() 
         return render(request, 'new_record.html', {'form':news})
             
    else:
        return redirect('home')

    

def customer_record(request, pk):
    if request.user.is_authenticated:
        #look up record with specific ID
        customer_record= Record.objects.get(id =pk)
        return render(request, 'customer_record.html', {'customer_record': customer_record})
    
    else:
        messages.success(request, 'You must be logged in')
        return redirect('home')
    

def update_record(request,pk):
    if request.user.is_authenticated:
        #query database with pk
        current_record = Record.objects.get(id=pk)
        form = AddRecord(instance=current_record)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'You have successfully updated the record')
                return redirect('home')
        return render(request, 'update_record.html', {'form':form})
    else:
        return redirect('home')
        


    



		