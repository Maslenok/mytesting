from django.contrib import auth
from django.template.context_processors import csrf
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView






class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register1.html"    # "register"  для стандартного вывода формы регистрации Django
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