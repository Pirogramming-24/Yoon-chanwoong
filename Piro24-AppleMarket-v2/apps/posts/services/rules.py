from .ocr_service import extract_words

def get_info(image):
    result = extract_words(image)
    result = result.split(' ')

    target = "탄수화물"
    indices = [i for i, s in enumerate(result) if target in s]
    try:
        indices = int(indices[0])
    except Exception as e:
        print(f"예상치 못한 에러: {e}")
    if indices:
        #print(f"찾은 위치: {indices}") # 결과: [3]
        carb = result[indices+1]
    
    target = "단백질"
    indices = [i for i, s in enumerate(result) if target in s]
    try:
        indices = int(indices[0])
    except Exception as e:
        print(f"예상치 못한 에러: {e}")
    if indices:
        #print(f"찾은 위치: {indices}") # 결과: [3]
        pro = result[indices+1]
    
    target = "지방"
    indices = [i for i, s in enumerate(result) if target in s]
    try:
        indices = int(indices[0])
    except Exception as e:
        print(f"예상치 못한 에러: {e}")
    if indices:
        #print(f"찾은 위치: {indices}") # 결과: [3]
        fat = result[indices+1]

    target = "kcal"
    indices = [i for i, s in enumerate(result) if target in s]
    try:
        indices = int(indices[0])
    except Exception as e:
        print(f"예상치 못한 에러: {e}")
    if indices:
        #print(f"찾은 위치: {indices}") # 결과: [3]
        kcal = result[indices-1]

    return kcal,carb,pro,fat


with open('/Users/yunchan-ung/Desktop/Yoon-chanwoong/Piro24-AppleMarket-v2/apps/posts/services/image.png', 'rb') as f:
    # Django의 파일 객체처럼 흉내내기 위해 읽기
    class MockFile:
        def __init__(self, file_data):
            self.file_data = file_data
        def read(self):
            return self.file_data

    mock_file = MockFile(f.read())
    k,c,p,f = get_info(mock_file)
    print(k,c,p,f)