from django.contrib import auth
from django.shortcuts import render
from result.models import Result


# Create your views here.
def result(request):
    user_result = auth.get_user(request)
    if request.user.is_authenticated():
        main_menu = "result"
        list_result=Result.objects.filter(users=user_result)
        title_name= " Результаты тестов которые Вы проходили"




        context = {"main_menu": main_menu,
                   "user_auth": user_result,
                   "list_result" : list_result,
                   "title_name" : title_name


                   }
        return render(request, 'result.html', context)






    else:
        main_menu = "result"
        error="Для получения результатв Вам надо зарегистрироваться"

        context = { "main_menu": main_menu,
                    "error": error,

                  }
        return render(request, 'result.html', context)