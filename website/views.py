from website.models import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate
from django.shortcuts import *
from django.template.loader import get_template
from django.contrib.auth.models import User
import logging
# Create your views here.


def try_login(request, current, after_success, after_failed):
    logger = logging.getLogger('django')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        logger.debug(str(request.POST))
        if form.is_valid():
            user = User.objects.get(username=form.cleaned_data['username'])

            if user.check_password(form.cleaned_data['password']):
                logger.debug("password correct in try_login")
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                logger.debug("pesel(username): " + form.cleaned_data['username'] + " password: " +
                            form.cleaned_data['password'] + " hash exist_user: " + form.cleaned_data['password'])
                login(request, user)
                logger.debug("loggin success")
                template = get_template(after_success)
                variables = RequestContext(request, {'user': user})
                output = template.rendeforor(variables)
                return HttpResponseRedirect("/")

        else:
            template = get_template(after_failed)
            variables = RequestContext(request, {'form': form})
            output = template.render(variables)
            logger.info("form invalid")
            return HttpResponse(output)
    form = LoginForm()
    logger.info("login get")
    template = get_template(current)
    variables = RequestContext(request, {'form': form})
    output = template.render(variables)
    return HttpResponse(output)


def home(request):
    return try_login(request, current="index.html", after_success="login.html", after_failed="index.html")


def clinic(request):
    return try_login(request, current="clinic.html", after_success='login.html', after_failed='index.html')


def doctor(request):
    return try_login(request, current="doctor.html", after_success='login.html', after_failed='index.html')


def pricing(request):
    return try_login(request, current="pricing.html", after_success='login.html', after_failed='index.html')


def contact(request):
    return try_login(request, current="contact.html", after_success='login.html', after_failed='index.html')


def register(request):
    logger = logging.getLogger('django')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            logger.debug("register post: " + str(request.POST) + " is valid")
            user = User.objects.create_user(
              username=form.cleaned_data['username'],
              password=form.cleaned_data['password'],
              email=form.cleaned_data['email']
            )
            user.is_active = True
            user.save()
            if user.check_password(form.cleaned_data['password']):
                logger.debug("user password: " + form.cleaned_data['password'] + " hash: " + user.password)
                logger.debug("username: " + form.cleaned_data['username'])
                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                logger.debug("user after auth: " + str(user))
                login(request, user)
                template = get_template("authenticated.html")
                variables = RequestContext(request, {'user': user})
                logger.info("User logged in")
                output = template.render(variables)
                return HttpResponse(output)
            else:
                logger.info("Wrong password")
        else:
            logger.debug("register post: " + str(request.POST) + " is invalid")
            return HttpResponseRedirect("contact.html")
    template = get_template("registration/register.html")
    form = RegisterForm()
    variables = RequestContext(request, {'form': form})
    output = template.render(variables)
    return HttpResponse(output)
