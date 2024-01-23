from datetime import datetime
import uuid
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from iblogs import settings
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from django.core.files.storage import default_storage
from django.core.files import File
from . tokens import generate_token

from blog.models import Gallery, Packages, Account


# Create your views here.
def services(request):
    return render(request, 'services.html', {})


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists!")
            return redirect('/signup')

        if User.objects.filter(email=email):
            messages.error(request, "Email already exists")
            return redirect('/signup')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 letters")
            return redirect('/signup')

        if pass1 != pass2:
            messages.error(request, "Password doesn't match")
            return redirect('/signup')

        if not username.isalnum():
            messages.error(request, "Username must contain only alphanumeric charachters!")
            return redirect('/signup')

        my_user = User.objects.create_user(username, email, pass1)
        my_user.first_name = fname
        my_user.last_name = lname
        my_user.is_active = False
        my_user.save()

        messages.success(request, "Your account has been successfully created ! \nWe have sent you a Confirmation "
                                  "Email\nPlease verify Your account")

        # Welcome Email
        current_site = get_current_site(request)
        email_subject = "Welcome Traveller, Confirm Your Email !!"
        message1 = render_to_string('email_confirm.html', {
            'name': my_user.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
            'token': generate_token.make_token(my_user)
        })

        email = EmailMessage(
            email_subject,
            message1,
            settings.EMAIL_HOST_USER,
            [my_user.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('/signin')

    return render(request, 'signup.html', {})


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, f"Hello, {fname}<br>Welcome to Travel")
            return redirect('/home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/signin')

    return render(request, 'signin.html', {})


def home(request):
    gals = Gallery.objects.all()
    data = {
        'gals': gals,
    }
    return render(request, 'home.html', data)


def about(request):
    return render(request, 'about.html', {})


def packages(request):
    # load all the posts from db
    packs = Packages.objects.all()
    if request.method=='GET':
        pack_title = request.GET.get('packsTilte')
        if pack_title:
            packs = Packages.objects.filter(title__icontains=pack_title)
    data = {
        'packs': packs,
    }
    return render(request, 'packages.html', data)


def package(request, url):
    packs = Packages.objects.get(url=url)
    return render(request, 'package.html', {'packs': packs})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        my_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        my_user = None

    if my_user is not None and generate_token.check_token(my_user, token):
        my_user.is_active = True
        my_user.save()
        login(request, my_user)
        return redirect('/signin')

    else:
        return render(request, 'active_failed.html')
    
def signout(request):
    logout(request)
    messages.success(request, 'You Have Been Logged Out successfully')
    return redirect('/signin')

def profile_edit(request):
    c_user = request.user
    fname = c_user.first_name
    lname = c_user.last_name
    uemail = c_user.email
    uname = c_user.username
    
    try:
        account = Account.objects.get(user=c_user)
    except Account.DoesNotExist:
        account = None
    
    if request.method=="POST":
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        new_image = request.FILES.get('image')
        country = request.POST.get('country')
        about = request.POST.get('about')
        
        
        if account:
            account.age = age
            account.phone = phone
            account.country = country
            account.about = about
            
            if new_image:
                
                if account.image:
                    default_storage.delete(account.image.name)
                    
                filename = default_storage.save(f'images/{c_user.username}_{new_image.name}', new_image)
                account.image = filename
                
            account.save()
        else:
            if new_image:
                filename = default_storage.save(f'images/{c_user.username}_{new_image.name}', new_image)
            else:
                filename = None
            new_account =  Account(user=c_user, age=age, phone=phone, country=country, about=about, image=filename)  
            
            new_account.save()
            
        return redirect('/profile')
        
    data = {
        'fname': fname,
        'lname': lname,
        'uemail': uemail,
        'uname': uname,
        'account': account,
    }
    return render (request, 'profile-edit.html', data)

def profile(request):
    c_user = request.user
    fname = c_user.first_name
    lname = c_user.last_name
    uemail = c_user.email
    try:
        acc = Account.objects.get(user=c_user)
    except Account.DoesNotExist:
        acc = None
    data = {
        'fname': fname,
        'lname': lname,
        'phone': acc.phone if acc else None,
        'age': acc.age if acc else None,
        'country': acc.country if acc else None,
        'about': acc.about if acc else None,
        'uemail':uemail,
        'image': acc.image if acc else None,
    }
    return render (request, 'profile.html', data)

def book(request):
    if request.method == 'POST':
        from_s = request.POST.get('from')
        destination = request.POST.get('destination')
        num = int(request.POST.get('num'))
        departure = request.POST.get('departure')
        arrival = request.POST.get('arrival')
        
        departure_str = datetime.strptime(departure, '%Y-%m-%d')
        arrival_str = datetime.strptime(arrival, '%Y-%m-%d')

        # Check if departure date is smaller than arrival date
        if departure_str >= arrival_str:
            messages.error(request, "We will try to take you in past in future, for now please select a future date😊")
            return redirect('/book')
        
        booking_data = {
            'from_s': from_s,
            'destination': destination,
            'num': num,
            'departure':departure,
            'arrival': arrival
            }
        request.session['booking_data'] = booking_data
        return redirect('/add_pass')
    return render(request, 'book.html', {})



def add_pass(request):
    booking_data = request.session.get('booking_data', None)
    
    if 'num' in booking_data:
        num_passengers = booking_data['num']
    else:
        num_passengers = 0 
    passengers = list(range(1, num_passengers + 1))
    
    context ={
        'booking_data': booking_data,
        'passengers': passengers
    }
    return render(request, 'add_passenger.html', context)


def review(request):
    booking_data = request.session.get('booking_data', None)
    
    if 'num' in booking_data:
        num_passengers = booking_data['num']
    else:
        num_passengers = 0
    
    c_user = request.user
    funame = c_user.first_name
    luname = c_user.last_name
    if request.method == "POST":
        source = request.POST.get('from')
        to = request.POST.get('to')
        fdate = request.POST.get('fdate')
        ldate = request.POST.get('ldate')
        fname = []
        lname = []
        age = []
        passengers = []
        
        for x in range(1, num_passengers+1):
            fname.append('fname'+str(x))
            fvar = fname[x-1]
            fvar = request.POST.get(fvar)
            lname.append('lname'+str(x))
            lvar = lname[x-1]
            lvar = request.POST.get(lvar)
            age.append('age'+str(x))
            var = age[x-1]
            var = request.POST.get(var)
            passenger = [fvar, lvar, var]
            passengers.append(passenger)
            
        booking_id = str(uuid.uuid4())
            
        current_site = get_current_site(request)
        email_subject = "Booking Confirmation - TRAVEL !!"
        message = render_to_string('booking.html', {
            'funame': funame,
            'luname': luname,
            'domain': current_site.domain,
            'source': source,
            'to': to,
            'fdate': fdate,
            'ldate': ldate, 
            'passengers': passengers,
            'booking_id': booking_id 
        })
        
        email = EmailMessage(
            email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [c_user.email],
        )
        email.fail_silently = True
        email.send()
        
        return redirect('/home')  
     
    return render(request, 'book.html', {}) 
        
        
    