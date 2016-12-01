from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.shortcuts import render,render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView

# Create your views here.

class RegisterFormView(FormView):
    form_class=UserCreationForm
    success_url="/index/"
    template_name="register.html"
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
    



def login(request):
    context={}
    context.update(csrf(request))
    return_path = request.META.get('HTTP_REFERER','/')
    if request.POST:
        username=request.POST.get("login","")
        password=request.POST.get("password","")
        user=auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
     #       return_path = request.META.get('HTTP_REFERER','/')
            auth.login(request,user)           
            return redirect(return_path)
        else:           
            context={
                "title_name": "Не верное имя либо пароль",
                "login_error" : True,                }                
            if user is None:
                return render(request, 'login.html', context)
    
    
    
    else:
        return redirect(return_path)




def logout (request):
    return_path = request.META.get('HTTP_REFERER','/')
    auth.logout(request)
    return redirect(return_path)