from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Course , Test



def index(request):
    course_list = Course.objects.order_by('course_name')
    context = {'course_list': course_list}
    return render(request, 'testing_code/index.html', context)

def course(request,course_url):
    course_id=Course(url=course_url).id
    course=get_object_or_404(Course, url=course_url)
    test_list=Test.objects.filter(curse_id=course_id)
    context={'test_list': test_list, 'url_page' : course_url }
    return render(request, 'testing_code/course.html', context)
 