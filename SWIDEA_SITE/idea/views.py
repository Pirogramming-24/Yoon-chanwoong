from django.shortcuts import render,redirect,get_object_or_404
from .models import Idea,Devtool
from django.contrib import messages

# Create your views here.
def main_page(request):
    ideas = Idea.objects.all()
    
    if request.method == 'POST':
        my_id = request.POST.get('zzim')
        target_idea = Idea.objects.get(id=my_id)
        target_idea.zzim = not target_idea.zzim
        target_idea.save()
    context = {
        'ideas':ideas
    }
    return render(request,'idea/main_page.html',context)

def detail_page(request,pk):
    idea = Idea.objects.get(id=pk)
    context = {
        'idea' : idea
    }
    if request.POST.get('button') == 'delete':
        idea.delete()
        print('del')
        return redirect('main')
    if 'zzim' in request.POST:
        my_id = request.POST.get('zzim')
        target_idea = Idea.objects.get(id=my_id)
        if target_idea.zzim:
            target_idea.zzim = False
        else:
            target_idea.zzim =True
        target_idea.save()
        print(target_idea.zzim)
        return redirect('detail',my_id)
    return render(request,'idea/detail_page.html',context)

def modify_page(request,pk):
    idea = Idea.objects.get(id=pk)
    devtools = Devtool.objects.all()
    if request.POST.get('button') == 'save':
        if request.POST.get('devtool') == 'empty':
            messages.warning(request,"개발툴을 먼저 등록하세요")
            return redirect('tool_register')
        devtool_id = request.POST.get('devtool')
        selected_tool = get_object_or_404(Devtool,id=devtool_id)
        idea.title = request.POST.get('title')
        if 'image' in request.FILES:
            idea.image = request.FILES.get('image')
        else:
            print("새로 업로드된 이미지가 없습니다.")
        idea.content = request.POST.get('content')
        idea.interest = request.POST.get('interest')
        idea.devtool = selected_tool
        idea.save()
        return redirect('detail', idea.id)
    elif request.POST.get('button') == 'delete_image':
        idea.image.delete(save=False)
    context = {
        'idea':idea,
        'devtools':devtools
    }
    return render(request,'idea/modify_page.html',context)

def register_page(request):
    devtools = Devtool.objects.all()
    if request.POST.get('button') == 'save':
        if request.POST.get('devtool') == 'empty':
            messages.warning(request,"개발툴을 먼저 등록하세요")
            return redirect('tool_register')
        devtool_id = request.POST.get('devtool')
        selected_tool = get_object_or_404(Devtool, id=devtool_id)
        Idea.objects.create(
            title = request.POST.get('title'),
            image = request.FILES.get('image'),
            content = request.POST.get('content'),
            interest = request.POST.get('interest'),
            devtool=selected_tool
        )
        return redirect('main')
    context = {
        'devtools':devtools
    }

    return render(request,'idea/register_page.html',context)

def tool_detail_page(request,pk):
    devtool = Devtool.objects.get(id=pk)
    context = {
        'devtool':devtool
    }
    if request.POST.get('button') == 'delete':
        devtool.delete()
        return redirect('tool_manage')
    return render(request,'idea/tool_detail_page.html',context)

def tool_manage_page(request):
    devtools = Devtool.objects.all()
    context = {
        'devtools':devtools
    }
    if request.POST.get('button') == 'delete_all':
        Devtool.objects.all().delete()
    return render(request,'idea/tool_manage_page.html',context)

def tool_modify_page(request,pk):
    devtool = Devtool.objects.get(id=pk)
    context = {
        'devtool':devtool
    }
    if request.POST.get('button') == 'save':
        devtool.name = request.POST.get('name')
        devtool.content = request.POST.get('content')
        devtool.kind = request.POST.get('kind')
        devtool.save()
        return redirect('tool_detail', devtool.id) 
    return render(request,'idea/tool_modify_page.html',context)

def tool_register_page(request):

    if request.method == 'POST':
        Devtool.objects.create(
            name = request.POST.get('name'),
            kind = request.POST.get('kind'),
            content = request.POST.get('content')
        )
        return redirect('tool_manage')
    return render(request,'idea/tool_register_page.html')