import requests
from django.shortcuts import render,redirect
from django.conf import settings
from .models import Reviews
import random
import json
import openai

fosters = []

def review_lists(request):
    api_key = settings.TMDB_API_KEY
    reviews = Reviews.objects.all()
    GENRE_MAP = {
        28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy",
        80: "Crime", 99: "Documentary", 18: "Drama", 10751: "Family",
        14: "Fantasy", 36: "History", 27: "Horror", 10402: "Music",
        9648: "Mystery", 10749: "Romance", 878: "SF", 10770: "TV Movie",
        53: "Thriller", 10752: "War", 37: "Western"
    }
    try:
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page=1"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        # print(f'data : {data}')

        movies = data.get('results',[]) #movies = data['results']
    except requests.exceptions.RequestException as e:
        print(f'api 에러 : {e}')
        movies = []

    if request.method == 'POST':
        action = request.POST.get('btn')
        if action == 'TMDB':
            reviewDB = Reviews.objects.all()
            for review in reviewDB:
                if review.isTMDB:
                    review.delete()
            for movie in movies:
                movie_id = movie.get('id')

                detail_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=ko-KR"
                detail_data = requests.get(detail_url).json()
                runtime = detail_data.get('runtime')

                credits_url = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}&language=ko-KR"
                credits_data = requests.get(credits_url).json()

                review_url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?api_key={api_key}&language=en-US&page=1"
                review_res = requests.get(review_url).json()
                tmdb_reviews = review_res.get('results', [])
                
                if tmdb_reviews:
                    first_review = tmdb_reviews[0]
                    content = first_review.get('content', '')
                    opinion_text = content[:500] + "..." if len(content) > 500 else content
                else:
                    opinion_text = "등록된 평론이 없습니다."

                director = [d.get('name') for d in credits_data.get('crew') if d.get('job') == 'Director'][0]
                actor = [a.get('name') for a in credits_data.get('cast')][:3]
                movie_score = round(float(movie['vote_average'])/2,1)


                genre_id = int(movie.get('genre_ids')[0])
                Reviews.objects.create(
                    title= movie['title'],
                    year=int(movie['release_date'][:4]),
                    score=movie_score,
                    image = movie['poster_path'],
                    movie_id = int(movie['id']),
                    genre = GENRE_MAP.get(genre_id),
                    hero = ", ".join(actor),
                    running_hour = runtime // 60,
                    running_minute = runtime % 60,
                    running_total = runtime,
                    director = director,
                    opinion = opinion_text
                )
            return redirect('review_lists')
        elif action == "search":
            searchVal = request.POST.get('q')
            reviewDB = Reviews.objects.all()
            for review in reviewDB:
                if(searchVal in review.title or
                   searchVal in review.hero or
                   searchVal in review.director):
                    review_id = review.id
                    break
                else:
                    review_id = 0
            if review_id != 0:
                return redirect('review_detail',review_id)
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
            isTMDB = False,
            title=request.POST.get('title'),
            year=request.POST.get('year'),
            director=request.POST.get('director'),
            hero=request.POST.get('hero'),
            genre=request.POST.get('genre'),
            score=request.POST.get('score'),
            running_hour = total_min // 60, 
            running_minute = total_min % 60, 
            running_total = total_min, 
            opinion = request.POST.get('opinion'),
            image = request.FILES.get('image')
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

def moviePage(request):

    api_key = settings.TMDB_API_KEY

    try:
        url = f"https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=ko-KR&page=1"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print(f'data : {data}')

        movies = data.get('results',[]) #movies = data['results']
    except requests.exceptions.RequestException as e:
        print(f'api 에러 : {e}')
        movies = []

    return render(request, 'movie/index.html', {'movies': movies})

def get_db_context():
    all_reviews = Reviews.objects.all()
    context = "영화 리뷰 데이터 목록:\n\n"
    for r in all_reviews:
        # 모델 필드에 맞춰 텍스트 구성
        source = "TMDB 데이터" if r.isTMDB else "직접 작성"
        context += f"### 영화: {r.title}, ({r.year}년 개봉)\n"
        context += f"- 출처: {source}\n"
        context += f"- 감독: {r.director} / 주연: {r.hero}\n"
        context += f"- 장르: {r.genre} / 평점: {r.score}점\n"
        context += f"- 상영시간: {r.running_hour}시간 {r.running_minute}분 (총 {r.running_total}분)\n"
        context += f"- 리뷰 및 의견: {r.opinion}\n"
        context += f"- TMDB ID: {r.movie_id}\n"
        context += "-----------------------------------\n"
    
    return context

def movie_chat_bot(request):
    answer = ""
    user_question = ""
    context_lst = request.session.get('chat_history', [])

    if request.method == "POST":
        if request.POST.get('AI') == 'reset':
            context_lst = []
            request.session['chat_history'] = []
            request.session.modified = True
        elif request.POST.get('AI') == "Go":
            user_question = request.POST.get('search_chat','')

            #내 데이터 베이스 정보 불러오기
            db_context = get_db_context()

            #AI불러오기 및 설정
            client = openai.OpenAI(
                api_key=settings.UPSTAGE_API_KEY,
                base_url="https://api.upstage.ai/v1/solar"
            )

            try:
                response = client.chat.completions.create(
                    model="solar-1-mini-chat",
                    messages=[
                        {
                            "role":"system",
                            "content": f"너는 사용자의 영화 DB를 분석하는 인공지능 비서야. 아래 제공된 영화 목록 데이터만을 근거로 사용자의 질문에 친절하게 답해줘.\n\n{db_context}"
                        },
                        {
                            "role":"user",
                            "content":user_question
                        }
                    ]
                )
                answer = response.choices[0].message.content
            except Exception as e:
                answer = f'에러가 발생함{str(e)}'

            request.session['chat_history'] = context_lst
            request.session.modified = True
        
            context_lst.append({
                'user_question':user_question,
                'answer':answer
            })
            
    return render(request,'movie/AI.html',{'context_lst':context_lst})