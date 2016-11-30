from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Course ,   Question
from django.contrib import auth


def course(request):
    course_list = Course.objects.order_by('course_name')
    title_name = "Доступные курсы"
    if request.user.is_authenticated():
        user_auth= True 
    else:
        user_auth=None 
    main_menu = "course"
    context = {'course_list': course_list, "title_name":title_name,"main_menu": main_menu , "user_auth": user_auth }
    return render(request, 'course.html', context)

def tests(request,course_name):
    course=get_object_or_404(Course, slug=course_name)    
    list_question=course.question_set.all()
    main_menu = "course"
    if request.user.is_authenticated():
        user_auth= True 
    else:
        user_auth=None 
    context={'test_list': list_question ,  "title_name":"Содержание курса:  ", "course":course, "main_menu": main_menu , "user_auth": user_auth }
    return render(request, 'tests.html', context)

def index(request):
    title_name = "Информация о нас "
    text='...На краю дороги стоял дуб. Он был, вероятно, в десять раз старше берез, составлявших лес, в десять раз толще и в два раза выше каждой березы. Это был огромный, в два обхвата дуб, с обломанными суками и корой, заросшей старыми болячками. С огромными, неуклюже, несимметрично растопыренными корявыми руками и пальцами, он старым, сердитым и презрительным уродом стоял между улыбающимися березами. Только он один не хотел подчиниться обаянию весны и не хотел видеть ни весны, ни солнца.'
    main_menu = "index"
    if request.user.is_authenticated():
        user_auth= True 
    else:
        user_auth=None           
    context = {'text': text, "title_name":title_name, "main_menu": main_menu , "user_auth": user_auth }
    return render(request, 'index.html', context)

 
def logout (request):
    auth.logout(request)
    return HttpResponseRedirect("/")
    
'''
def course(request, course_name):
    now=course_name
    html="<html><body>Вывод названия курса %s. </body></html>" % now
    return HttpResponse(html )
'''
# class="active"
# {{if (main_menu=='course')}} class="active"{{/if}}