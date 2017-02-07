import datetime
from .models import Setup



def site_setup(request):
    try:
        qss = Setup.objects.all().first()
    except:
        qss = None
    if request.path == '/':
        home = True
    else:
        home = False
    return {
        'SETUP': qss,
        'CURRENT_YEAR': datetime.datetime.now(),
        'HOME_PAGE': home,
    }
