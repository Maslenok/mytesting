from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from .models import Course ,   Question, Answer
from result.models import Result
from django.contrib import auth
from django.template.context_processors import csrf
from result.models import UsersAnswer
from django.db.models import  Max




def index(request):
    title_name = "Информация о нас "
    text='...На краю дороги стоял дуб. Он был, вероятно, в десять раз старше берез, составлявших лес, в десять раз толще и в два раза выше каждой березы. Это был огромный, в два обхвата дуб, с обломанными суками и корой, заросшей старыми болячками. С огромными, неуклюже, несимметрично растопыренными корявыми руками и пальцами, он старым, сердитым и презрительным уродом стоял между улыбающимися березами. Только он один не хотел подчиниться обаянию весны и не хотел видеть ни весны, ни солнца.'
    main_menu = "index"

    context = {'text': text,
               'title_name':title_name,
               'main_menu': main_menu ,
               'user_auth': auth.get_user(request).username,
                }
    return render(request, 'index.html', context)



def course(request):
    course_list = Course.objects.order_by('course_name')
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
    title_name="Содержание курса"    
    context={'test_list': list_question ,  
             'title_name': title_name, 
             'course' : course, 
             'main_menu': main_menu , 
             'user_auth': user_auth,
             "course_name" :course_name,
             }
    return render(request, 'tests.html', context)


def question(request,course_name):
    course = get_object_or_404(Course, slug=course_name)
    context = {}
    context.update(csrf(request))
    main_menu = "course"

    if request.user.is_authenticated():
        user_auth = True
        user_question = auth.get_user(request)
    else:
        return redirect("/auth/login/")



    if request.POST.get("question_cur","") and user_auth :         # если запрос пришел из формы
        question_cur_id = int(request.POST.get("question_cur", ""))
        result = int(request.POST.get("result", ""))
        question_next_id = Question.get_next_question_id(course, question_cur_id)
        answer_in_question=Answer.answers_in_question(question_cur_id)

        correct_answer = False

        for answer in answer_in_question:
            answer_arr="answer_arr_" + str(answer.pk)
            if int(request.POST.get(answer_arr, "")) == 1 :
                correct_answer = True



        UsersAnswer(users=user_question,
                    course=course,
                    question=Question.objects.get(id=question_cur_id),
                    result=Result.objects.get(id=result),
                    right=correct_answer).save()





        if question_next_id == None: # проверка на то что вопрос был посленим . None если последним
            result_end=Result.objects.get(id=result)
            result_end.is_complete=True
            result_end.save()



            # тут бедет среднее и переход на  страницу результата
            context = {
                "course": course,
                "main_menu": main_menu,
                "user_auth": user_auth,
            }
            return render(request, 'testing_end.html', context)


        else:  # если вопрос был не последним

            result_id=result


    else: # Если запрос  не пост
        list_question = UsersAnswer.objects.filter(users=request.user, course=course)

    # Попробовать через if not object



        try:
            Result.objects.get(users=user_question, course=course, is_complete=False)  # если уже отвечали
            question_cur_id = list_question.aggregate(Max('question'))["question__max"]
            question_next_id = Question.get_next_question_id(course, question_cur_id)
            result_id=Result.objects.get(users=user_question, course=course, is_complete=False).id

        except ObjectDoesNotExist:
            question_cur_id = 0
            question_next_id = Question.get_next_question_id(course, question_cur_id)
            Result_new = Result(users=user_question, course=course)
            Result_new.save()
            result_id = int(Result_new.id)

    answer_list = Answer.answers_in_question(question_next_id)

    context = {
            "course": course,
            "main_menu": main_menu,
            "question": Question.objects.get(id=question_next_id),
            "question_cur_id": question_next_id,
            "user_auth": user_auth,
            "answer_list": answer_list,
            "result": result_id,
           }
    return render(request, 'testing.html', context)


