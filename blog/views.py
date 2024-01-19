from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from iblogs import settings
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode
from django.utils.http import urlsafe_base64_decode
from . tokens import generate_token

from blog.models import Gallery, Packages, Services


# Create your views here.
def book(request):
    return render(request, 'book.html', {})


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
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')

        if User.objects.filter(username=username):
            messages.error(request, "Username already exists!")
            return redirect('/')

        if User.objects.filter(email=email):
            messages.error(request, "Email already exists")
            return redirect('/')

        if len(username) > 10:
            messages.error(request, "Username must be under 10 letters")
            return redirect('/')

        if pass1 != pass2:
            messages.error(request, "Password doesn't match")
            return redirect('/')

        if not username.isalnum():
            messages.error(request, "Username must contain only alphanumeric charachters!")
            return redirect('/')

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
    data = {
        'packs': packs,
    }
    return render(request, 'packages.html', data)


def package(request, url):
    packs = Packages.objects.get(url=url)
    print(packs)
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
        return redirect('/home')

    else:
        return render(request, 'active_failed.html')
