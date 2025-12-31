from django.shortcuts import render,redirect
from .models import Reviews

def review_lists(request):
	reviews = Reviews.objects.all()
	context = {
		'reviews' : reviews
    }
	return render(request,"movie/review_lists.html",context)

def review_detail(request):
	return render(request,"movie/review_detail.html")

def review_write_modify(request):
    if request.method == 'POST':
        # 1. 사용자가 input에 입력한 값들을 가져옵니다.
        title = request.POST.get('title')
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        director = request.POST.get('director')
        score = request.POST.get('score')

        # 2. DB에 저장합니다.
        # director를 비워두면 models.py에 설정한 default값이 들어갑니다.
        Reviews.objects.create(
            title=title,
            year=year,
            genre=genre,
            director=director if director else '미상', # 비어있으면 직접 지정 가능
            score=score if score else 0.0
        )

        # 3. 저장이 끝나면 목록 페이지로 보냅니다.
        return redirect('review_lists')

    # GET 요청일 때는 작성 페이지를 보여줍니다.
    return render(request, "movie/write_modify.html")