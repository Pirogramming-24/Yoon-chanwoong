# import torch
# from transformers import pipeline

# def analyze_sentiment_AI():
#     device = "mps" if torch.backends.mps.is_available() else "cpu"
#     model_id = "nlptown/bert-base-multilingual-uncased-sentiment"
#     classifier = pipeline(
#         "sentiment-analysis", 
#         model=model_id, 
#         device=device
#     )
#     return classifier

# def analyze_sentiment_AI_run(classifier,review):

#     print("\n🚀 분석 결과:")
#     result = classifier(review)[0]
#     label = result['label']  # 예: '5 stars'
#     score = result['score']  # 확신도
    
#     print(f"📝 리뷰: {review}")
#     print(f"⭐ 예측 평점: {label} (확신도: {score:.2f})")
#     print("-" * 30)

# if __name__ == "__main__":
#     reviews = [
#        "This is truly my all-time favorite movie! It was so moving.",
#         "It’s a total waste of time. Don’t watch it.",
#         "It was just okay. Decent enough as a time-killer."
#     ]
#     classifier = analyze_sentiment_AI()
#     for review in reviews:
#         analyze_sentiment_AI_run(classifier,review)