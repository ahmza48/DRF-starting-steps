from django.http import HttpResponse

def home_page(request):
    print('Home page requested!')
    return HttpResponse('--------------THIS IS  HOME PAGE--------------')