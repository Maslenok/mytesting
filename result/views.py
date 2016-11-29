from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def result(request):
    main_menu = "result"
    context = { "main_menu": main_menu  ,}
    return render(request, 'result.html', context)