from django.shortcuts import render,redirect
from .models import Reviews
import random

fosters = []

def review_lists(request):
    reviews = Reviews.objects.all()
    context = {
        'reviews' : reviews
    }
    return render(request,"movie/review_lists.html",context)

def review_detail(request,pk):
    review = Reviews.objects.get(id = pk)
    context = {
         'review' : review
    }
    if request.method == 'POST' and request.POST.get('delete') == 'delete':
        review.delete()
        return redirect('review_lists')
        
    return render(request,"movie/review_detail.html",context)

def review_write(request):
    if request.method == 'POST':
        # 1. 사용자가 입력한 총 '분'을 가져옴 (예: 135)
        raw_time = request.POST.get('running_time')
        total_min = int(raw_time) if raw_time and raw_time.isdigit() else 0

        # 2. 직접 계산해서 각각 필드에 할당
        Reviews.objects.create(
            title=request.POST.get('title'),
            year=request.POST.get('year'),
            director=request.POST.get('director'),
            hero=request.POST.get('hero'),
            genre=request.POST.get('genre'),
            score=request.POST.get('score'),
            running_hour = total_min // 60, 
            running_minute = total_min % 60, 
            running_total = total_min, 
            opinion = request.POST.get('opinion')
        )
        return redirect('review_lists')
    return render(request, "movie/write.html")

def review_modify(request, pk):
    review = Reviews.objects.get(id=pk)
    if request.method == 'POST':
        raw_time = request.POST.get('running_time')
        total_min = int(raw_time) if raw_time and raw_time.isdigit() else 0

        review.title = request.POST.get('title')
        review.year = request.POST.get('year')
        review.genre = request.POST.get('genre')
        review.score = request.POST.get('score')
        review.running_hour = total_min // 60
        review.running_minute = total_min % 60
        review.running_total = total_min
        review.opinion = request.POST.get('opinion')
        review.director = request.POST.get('director')
        review.hero = request.POST.get('hero')
        review.save()
        return redirect('review_lists')
    return render(request, "movie/modify.html", {"review": review})

def delete(request):
    reviews = request.POST.all()
    for i in reviews:
        i.delete()