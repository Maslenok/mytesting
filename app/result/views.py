from django.contrib import auth
from django.shortcuts import render

from app.result.models import Result


def result(request):
    user_result = auth.get_user(request)
    if request.user.is_authenticated():
        main_menu = "result"
        title_name = " Результаты тестов которые Вы проходили"
        context = {"main_menu": main_menu,
                   "user_auth": user_result,
                   "title_name": title_name
                   }
        if  Result.objects.filter(users=user_result, is_complete=True).count()>0:
            list_result = Result.objects.filter(users=user_result, is_complete=True)
            context["list_result"]=list_result
        else:
            error='Вы еще не проходили тесты'
            context["error"]=error
        return render(request, 'result.html', context)
    else:
        main_menu = "result"
        error="Для получения результатв Вам надо зарегистрироваться"

        context = { "main_menu": main_menu,
                    "error": error,
                  }
        return render(request, 'result.html', context)