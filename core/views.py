from django.shortcuts import render

# Create your views herse.


def index(request):
    return render(request, 'test.html')
