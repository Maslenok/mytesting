# coding=utf-8
#from annoying.decorators import ajax_request
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.context_processors import csrf
from django.views.generic import UpdateView

from core.admin import UserCreationForm
from core.forms import UserProfileForm
from core.models import Setup, User
from django.views.generic.edit import FormView
from django import forms





def get_robots_txt(request):
    try:
        content = Setup.objects.all()[0].robots_txt
    except:
        content = u'User-agent: *'
    robots_response = HttpResponse(content, content_type='text/plain')
    return robots_response


#@ajax_request
def landing_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    error = u'Вы ввели неверный e-mail или пароль'
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect(request.META['HTTP_REFERER'])
        else:
            return {
                'error': error
            }
    else:
        return {
            'error': error
        }

#@ajax_request
def landing_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            exist_user = User.objects.get(email=username)
        except:
            exist_user = None
        if exist_user:
            return {
                'error': u'Пользователь с таким email уже зарегистрирован в системе!'
            }
        else:
            user = User.objects.create_user(username, password)
            user.is_staff = True
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth.login(request, user)
            return {
                'success': u'Вы успешно зарегистрировались на сайте!'
            }


class UserUpdateView(UpdateView):
    model = User
    template_name = 'profile.html'
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user






class RegisterFormView(FormView):
    form_class = UserCreationForm
    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"
    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"    # "register"  для стандартного вывода формы регистрации Django
    #template_name = "register1.html"
    def form_valid(self, form):
        form.save()
        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


def login(request):
    context={}
    context.update(csrf(request))
    try:
        request.session['return_url']
        return_path=request.session['return_url']
    except:
        return_path =request.META.get('HTTP_REFERER','/')
    if request.POST:
        username=request.POST.get("username","")
        password=request.POST.get("password","")
        user=auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            return redirect(return_path)
        else:
            request.session['return_url']=return_path
            context={
                "login_error" : True,
                    }
            return render(request, 'login.html', context)
    else:
        try:
            request.session['return_url']
            urls = request.session["return_url"]
        except:
            urls = "/"
        return redirect(urls)

def logout (request):
    return_path = request.META.get('HTTP_REFERER','/')
    auth.logout(request)
    return redirect(return_path)