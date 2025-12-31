from django.shortcuts import render,redirect
from .models import Reviews

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
        # 1. 사용자가 input에 입력한 값들을 가져옵니다.
        title = request.POST.get('title')
        year = request.POST.get('year')
        director = request.POST.get('director')
        hero = request.POST.get('hero')
        genre = request.POST.get('genre')
        score = request.POST.get('score')
        running_time = request.POST.get('running_time')

        # 2. DB에 저장합니다.
        # director를 비워두면 models.py에 설정한 default값이 들어갑니다.
        Reviews.objects.create(
            title=title,
            year=year,
            director=director,
            hero=hero,
            genre=genre,
            score=score,
            running_time=running_time
        )

        # 3. 저장이 끝나면 목록 페이지로 보냅니다.
        return redirect('review_lists')

    # GET 요청일 때는 작성 페이지를 보여줍니다.
    return render(request, "movie/write.html")

def review_modify(request,pk):
    review = Reviews.objects.get(id=pk)
    context = {
         "review" : review
    }
    if request.method == 'POST':
        review.title = request.POST.get('title')
        review.year = request.POST.get('year')
        review.genre = request.POST.get('genre')
        review.score = request.POST.get('score')
        review.running_time = request.POST.get('running_time')
        review.opinion = request.POST.get('opinion')
        review.director = request.POST.get('director')
        review.hero = request.POST.get('title')
        review.save()
        return redirect('review_lists')
    return render(request, "movie/modify.html",context)

def delete(request):
    reviews = request.POST.all()
    for i in reviews:
        i.delete()