from django.shortcuts import render,redirect
import torch
from transformers import pipeline,AutoModelForSeq2SeqLM,AutoTokenizer
from django.contrib.auth import get_user_model
from diffusers import DiffusionPipeline
from diffusers import StableDiffusionXLPipeline, UNet2DConditionModel, EulerAncestralDiscreteScheduler
from huggingface_hub import hf_hub_download
import time

User = get_user_model()

# Create your views here.

# ==========================================================================================
# <analyze_sentiment_AI 모델 불러오기>
def analyze_sentiment_AI():
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    model_id = "nlptown/bert-base-multilingual-uncased-sentiment"
    classifier = pipeline(
        "sentiment-analysis", 
        model=model_id, 
        device=device
    )
    return classifier

classifier = analyze_sentiment_AI()

def analyze_sentiment_AI_run(classifier,review):
    result = classifier(review)[0]
    label = result['label']  # 예: '5 stars'
    score = result['score']  # 확신도
    return f"⭐ 예측 평점: {label} (확신도: {score:.2f})"

# ==========================================================================================

# ==========================================================================================
# <summarizationAI 모델 불러오기>
# 1. 모델 설정 (google/pegasus-xsum)
trans_model_name = "google/pegasus-xsum"
# 2. 장치 설정 (MacBook Air의 GPU인 MPS 사용)
device = "mps" if torch.backends.mps.is_available() else "cpu"
# 3. 모델 및 토크나이저 로드
trans_tokenizer = AutoTokenizer.from_pretrained(trans_model_name)
trans_model = AutoModelForSeq2SeqLM.from_pretrained(trans_model_name).to(device)
# 요약 파이프라인 구축
summarizer = pipeline(
    "summarization", 
    model=trans_model, 
    tokenizer=trans_tokenizer, 
    device=device
)
# ==========================================================================================

# ==========================================================================================
# <text-generation AI 모델 불러오기>
generator = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-1.7B-Instruct", device_map="auto")
# ==========================================================================================

def main(request):
    return render(request,'AI/main.html')

def AI_one_page(request):
    if request.user.is_authenticated:
        answers = request.user.AI_one_Chatting
    elif request.method == "GET":
        request.session['answers'] = []
        answers = []
    else:
        answers = request.session['answers']
    context = {
        'answers':answers
    }
    if request.method == "POST":
        article = request.POST.get('search')
        output = analyze_sentiment_AI_run(classifier,article)
        answers.append({'article':article,'output':output})
        if request.user.is_authenticated:
            request.user.save()
        else:
            request.session['answers'] = answers
    
    return render(request,'AI/AI_one.html',context)

def AI_two_page(request):
    if not request.user.is_authenticated:
        return redirect('user:login')
    
    answers = request.user.AI_two_Chatting
    context = {
        'answers':answers
    }
    if request.method == "POST":
        article = request.POST.get('search')
        result = summarizer(
            article,
            max_length=60,
            min_length=20,
            do_sample=False
        )
        answers.append({'article':article,'output':result[0]['summary_text']})
        print(answers)
        request.user.save()
    
    return render(request,'AI/AI_two.html',context)

def AI_three_page(request):
    if not request.user.is_authenticated:
        return redirect('user:login')
    answers = request.user.AI_three_Chatting
    context = {
        'answers':answers
    }
    if request.method == "POST":
        article = request.POST.get('search')
        messages = [{"role": "user", "content": article}]
        output = generator(messages, max_new_tokens=100)[0]['generated_text'][-1]['content']
        answers.append({'article':article,'output':output})
        request.user.save()
    
    return render(request,'AI/AI_three.html',context)