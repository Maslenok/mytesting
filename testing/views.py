from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Course ,   Question, Answer, AboutPage
from result.models import Result
from django.contrib import auth
from django.template.context_processors import csrf
from result.models import UsersAnswer
from django.db.models import  Max

def index(request):
    title_name = "Информация о нас "
    main_menu = "index"
    if AboutPage.objects.filter(is_active=True).count() >=1:
        index= AboutPage.objects.filter(is_active=True)[0]
        context = {'text': str(index.about),
                   'title_name': title_name,
                   'main_menu': main_menu,
                   'user_auth': auth.get_user(request).username,
                   }
    else:
        context = {
               'title_name':title_name,
               'main_menu': main_menu ,
               'user_auth': auth.get_user(request).username,
                }
    return render(request, 'index.html', context)

def course(request):
    course_list = Course.objects.order_by('courseName')
    title_name = "Доступные курсы"

    if request.user.is_authenticated():
        user_auth= True
    else:
        user_auth=None
    main_menu = "course"
    context = {'course_list': course_list,
               'title_name':title_name,
               'main_menu': main_menu ,
               'user_auth': user_auth,
               }
    return render(request, 'course.html', context)

def tests(request,course_name):
    course=get_object_or_404(Course, slug=course_name)
    list_question=course.question_set.all()

    if request.user.is_authenticated():
        user_auth= True
    else:
        user_auth=None
    main_menu = "course"
    title_name="Вы смотрите курс :  "
    context={'test_list': list_question ,
             'title_name': title_name,
             'course' : course,
             'main_menu': main_menu ,
             'user_auth': user_auth,
             "course_name" :course_name,
             }
    return render(request, 'tests.html', context)



def question(request,course_name):

        if not request.user.is_authenticated():  # если пользователь не зарегистрирован переход на страницу логин
            return redirect("/auth/login/")

        course = get_object_or_404(Course, slug=course_name)

        context = {}
        context.update(csrf(request))
        context = {
            "main_menu":"course",
            "user_auth": request.user.is_authenticated(),
            "course": course,
        }
        if request.POST.get("question_cur", "") and request.user.is_authenticated():  # если метод POST, и мы проходим курс
            question_cur_id = int(request.POST.get("question_cur", ""))
            question_next_id = Question.get_next_question_id(course, question_cur_id)
            result_id = int(request.POST.get("result", ""))
            answer_in_question_len = Answer.answers_in_question(question_cur_id).count()
            list_answers_right_id = []
            for answer in Answer.objects.filter(question=question_cur_id, is_correct=True):
                list_answers_right_id.append(answer.id)

            if len(request.POST.getlist("answer_id_list")) == 0:
                error_message = " Надо отметить как минимум  один ответ"

            if len(request.POST.getlist("answer_id_list")) == answer_in_question_len:
                error_message = " Все ответы не могут быть прравильные"

            if "error_message" in locals():
                question_next_id = question_cur_id
                context["error_message"]= error_message
            else:
                if len(request.POST.getlist("answer_id_list")) == len(list_answers_right_id):
                    for answer_id in request.POST.getlist("answer_id_list"):
                        if list_answers_right_id.count(int(answer_id)) >= 1:
                            correct_answer = True
                        else:
                            correct_answer = False
                            break
                else:
                    correct_answer = False

                UsersAnswer(users=auth.get_user(request),
                            course=course,
                            question=Question.objects.get(id=question_cur_id),
                            result=Result.objects.get(id=result_id),
                            right=correct_answer
                            ).save()

            if Question.get_next_question_id(course, question_cur_id) == None:  # проверка на то что вопрос последний . None если последний.
                                          # сохраняем результат и переходим на страницу результатов

                all_users_answers_count = UsersAnswer.objects.filter(result=result_id,
                                                               users=auth.get_user(request),
                                                               ).count()

                correct_users_answer_count = UsersAnswer.objects.filter(result=result_id,
                                                                  users=auth.get_user(request),
                                                                  right=True).count()

                print (all_users_answers_count, "all_users_answers_count")
                print (correct_users_answer_count,"correct_users_answer_count" )
                result_value =int((correct_users_answer_count / all_users_answers_count) * 100)
                print(result_value, "result_value")
                result_end = Result.objects.get(id=result_id)
                result_end.is_complete = True
                result_end.resultValue = result_value
                result_end.save()

                context["main_menu"] = "result"
                context["title_name"]="Результаты тестирования "
                context["output_result"] = True
                context["result_value"] = result_value

                return render(request, 'result.html', context)

        else: # если метод не POST (пришли по внешней ссылке) или перешли со страници описания курса
            course = Course.objects.get(slug=course_name)  #  !!!!!!!!!!!! потом проверить заменить на верхний
            if Course.questions_course(course).count() == 0:   #  В кусе нет вопросов
                context["questions_asked"]= True
                return render(request, 'testing.html', context)
            else:  # Вопросы в курсе есть

                print("Выпадаем при новом прохождении или тесте",auth.get_user(request),"Имя пользователя" )
                print("course", course.id)
              #  Result.objects.get(users=auth.get_user(request), is_complete= False, course=course)
                print("Прошли точку создания обекта")
                try:     # если на вопросы курса отвечали , но не закончили тест
                    res= Result.objects.get(users=auth.get_user(request), course=course,is_complete=False)
                    print(Result.objects.get(users=auth.get_user(request), course=course,is_complete=False), "Тестирование")
                    result_obj = Result.objects.get(users=auth.get_user(request), course=course,
                                                           is_complete=False)
                    list_question_saved = UsersAnswer.objects.filter(users=auth.get_user(request), course=course,result=result_obj.id , is_complete=False)
                    question_cur_id = list_question_saved.aggregate(Max('question'))["question__max"]
                    question_next_id = Question.get_next_question_id(course, question_cur_id)
                    result_id=result_obj.id
                    print("Продолжить тестирование")



                except:  # тест не проходили или прошли и закончили
                    question_cur_id = 0
                    question_next_id = Question.get_next_question_id(course, question_cur_id)
                    Result_new = Result(users=auth.get_user(request), course=course, is_complete=False)
                    Result_new.save()
                    result_id=int(Result_new.id)
                    print("Начать тестирование заново" )

        context["result"] = result_id
        context["answer_list"]= Answer.answers_in_question(question_next_id)
        context["question_cur_id"] = question_next_id
        context["question"] = Question.objects.get(id=question_next_id)
        return render(request, 'testing.html', context)