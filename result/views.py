
from django.shortcuts import render


# Create your views here.
def result(request):
    main_menu = "result"
    context = { "main_menu": main_menu  ,}
    return render(request, 'result.html', context)