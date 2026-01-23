from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Post,Story
from django.http import JsonResponse

User = get_user_model()

# Create your views here.

def mainPage(request):
    if not request.user.is_authenticated:
        return redirect('user:login')
    users = User.objects.all().exclude(id=request.user.id)
    posts = Post.objects.all().order_by('-id')
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        print(post_id)
        if post_id:
            # filter(user=request.user)를 붙여서 '내가 쓴 글'만 찾아 지우도록 제한합니다.
            post_to_delete = Post.objects.filter(id=post_id, user=request.user).first()
            if post_to_delete:
                post_to_delete.delete()
            return redirect('insta:mainPage')
        
    context = {
        'users':users,
        'posts':posts
    }

    return render(request,'insta/mainPage.html',context)

def profile(request,pk):
    user = User.objects.get(id=pk)
    posts = Post.objects.filter(user=user)
    context = {
        'user_profile':user,
        'posts':posts
    }
    return render(request,'insta/profile.html',context)

def follow(request,pk):
    follower_id = request.user.id
    followed_id = pk
    follower = User.objects.get(id=follower_id) #아싸
    followed = User.objects.get(id=followed_id) #인싸
    follower.followGuys.add(followed) #아싸가 인싸 팔로우
    followers_num = follower.followGuys.count() #아싸의 팔로잉 수
    followed_num = followed.followers.count() #인싸의 팔로워 수
    print(followers_num,followed_num)
    return redirect('insta:mainPage')

def unfollow(request, pk):
    follower = request.user 
    followed = User.objects.get(id=pk)
    if follower.followGuys.filter(id=followed.id).exists():
        follower.followGuys.remove(followed)
    print(f"나의 팔로잉 수: {follower.followGuys.count()}, 저 분의 팔로워 수: {followed.followers.count()}")
    return redirect('insta:mainPage')

def makepost(request):
    if request.method == "POST":
        photo = request.FILES.get('photo')
        content = request.POST.get('content')
        Post.objects.create(
            user_id = request.user.id,
            photo=photo,
            content=content
        )
        return redirect('insta:mainPage')
    return render(request,'insta/makepost.html')

def modify(request,pk):
    # 1. 수정할 게시물을 가져옵니다. (없으면 404)
    post = get_object_or_404(Post, id=pk)
    
    # 보안: 작성자 본인이 아니면 메인으로 튕겨내기
    if post.user != request.user:
        return redirect('insta:mainPage')

    if request.method == "POST":
        # 2. 수정된 데이터를 저장 (POST 방식)
        if request.FILES.get('photo'): # 사진을 새로 올렸을 때만 교체
            post.photo = request.FILES.get('photo')
            
        content = request.POST.get('content')
        photo = request.FILES.get('photo') 
        
        post.content = content
        if photo: # 새로운 사진이 업로드된 경우에만 업데이트
            post.photo = photo
            
        post.save()
        return redirect('insta:mainPage')
    return render(request,'insta/modify.html', {'post': post})

def post_like_ajax(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if post.joayo.filter(id=user.id).exists():
        # 이미 좋아요를 누른 유저라면 -> 좋아요 취소
        post.joayo.remove(user)
        message = "removed"
    else:
        # 아직 안 누른 유저라면 -> 좋아요 추가
        post.joayo.add(user)
        message = "added"

    context = {
        'like_count': post.joayo.count(), # 전체 좋아요 개수
        'message': message,
    }
    return JsonResponse(context)

def makestory(request):
    if request.method == "POST":
        photo = request.FILES.get('photo')
        Story.objects.create(
            user = request.user,
            photo = photo
        )
        return redirect('insta:mainPage')
    return render(request,'insta/story.html')
