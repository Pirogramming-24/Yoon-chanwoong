from django.shortcuts import render,HttpResponse
from .models import Idea

# Create your views here.
def main_page(request):
    return render(request,'idea/main_page.html')

def detail_page(request):
    return render(request,'idea/detail_page.html')

def modify_page(request):
    return render(request,'idea/modify_page.html')

def register_page(request):
    if request.POST.get('button') == 'save':
        Idea.objects.create(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            content = request.POST.get('content'),
            interest = request.POST.get('interest'),
            devtool = request.POST.get('devtool')
        )
    elif request.POST.get('button') == 'delete':
        Idea.objects.all().delete()

    return render(request,'idea/register_page.html')

def tool_detail_page(request):
    return render(request,'idea/tool_detail_page.html')

def tool_manage_page(request):
    return render(request,'idea/tool_manage_page.html')

def tool_modify_page(request):
    return render(request,'idea/tool_modify_page.html')

def tool_register_page(request):
    return render(request,'idea/tool_register_page.html')