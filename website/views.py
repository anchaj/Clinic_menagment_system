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
        log_str = ""
        form = LoginForm(request.POST)
        if form.is_valid():
            log_str = log_str.join("\nform valid:")
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            log_str = log_str.join("username: ").join(form.cleaned_data['username']).join("\n")
            log_str = log_str.join("password: ").join(form.cleaned_data['password']).join("\n")
            login(request, user)
            logger.info("loggin success")
            template = get_template(after_success)
            variables = RequestContext(request, {'user': user})
            output = template.render(variables)
            logger.info(log_str)
            return HttpResponseRedirect("/")
        else:
            log_str = log_str.join("\nform invalid")
            template = get_template(after_failed)
            variables = RequestContext(request, {'form': form})
            output = template.render(variables)
            logger.info(log_str)
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
    logger_str = ""
    if request.method == "POST":
        try:
            logger_str += "register post: " + str(request.POST) + " is "
            form = RegisterForm(request.POST)
            if form.is_valid():
                logger_str += "valid"
                user = User.objects.create_user(
                  username=form.cleaned_data['pesel'],
                  password=form.cleaned_data['password'],
                  email=form.cleaned_data['email']
                )
                user.save()
                template = get_template("registration/login.html")
                variables = RequestContext(request, {})
                output = template.render(variables)
                logger.info(logger_str)
                return HttpResponse(output)
            else:
                logger_str += "invalid"
                logger.info(logger_str)
                return HttpResponseRedirect("contact.html")
        finally:
            logger.info(logger_str)
    template = get_template("registration/register.html")
    form = RegisterForm()
    variables = RequestContext(request, {'form': form})
    output = template.render(variables)
    return HttpResponse(output)
