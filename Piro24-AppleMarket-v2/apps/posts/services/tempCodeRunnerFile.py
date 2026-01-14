sult.split(' ')

    target = "탄수화물"

    # "탄수화물"이 포함된 모든 요소의 인덱스 찾기
    indices = [i for i, s in enumerate(result) if target in s]

    if indices:
        print(f"찾은 위치: {indices}") # 결과: [3]
    print(f"OCR 결과: {result}")