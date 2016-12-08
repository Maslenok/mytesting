from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render,render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
#from django import olforms


# Create your views here.

class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)





def login(request):
    context={}
    context.update(csrf(request))
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
        if "return_url" in request.session:
            urls= request.session["return_url"]
        else:
            urls="/"    
        return redirect(urls)




def logout (request):
    return_path = request.META.get('HTTP_REFERER','/')
    auth.logout(request)
    return redirect(return_path)