from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Course ,   Question



def index(request):
    course_list = Course.objects.order_by('course_name')
    context = {'course_list': course_list}
    return render(request, 'testing_code/index.html', context)

def course(request,course_url):
    course=get_object_or_404(Course, url=course_url)
    course_odj=Course.objects.get(url=course_url)
    questio_list=Question.objects.filter(curse_id=course_odj.id)
    context={'test_list': questio_list, 'url_page' : course_url, 'url_course': course_odj.id }
    return render(request, 'testing_code/course.html', context)
 