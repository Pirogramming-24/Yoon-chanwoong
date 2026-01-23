from transformers import AutoTokenizer,AutoModelForSeq2SeqLM

#모델명
trans_model_name = 'facebook/nllb-200-distilled-600M'
#토크나이저랑 모델 로드
trans_tokenizer = AutoTokenizer.from_pretrained(trans_model_name)
trans_model = AutoModelForSeq2SeqLM.from_pretrained(trans_model_name)
#입력 언어 설정
trans_tokenizer.src_lang = "kor_Hang"

def translatorAI(input_text):
    #입력 텍스트 토큰화
    inputs = trans_tokenizer(input_text, return_tensors="pt")

    #번역 생성
    translated_tokens = trans_model.generate(
        **inputs,
        forced_bos_token_id=trans_tokenizer.convert_tokens_to_ids("eng_Latn"),
        max_length=30
    )

    return trans_tokenizer.batch_decode(translated_tokens, skip_special_tokens=True)[0]

print(translatorAI('요새 날씨가 너무 춥다'))
print(translatorAI('반갑습니다 김정은입니다'))
print(translatorAI('당신은 정말 아름다워요'))