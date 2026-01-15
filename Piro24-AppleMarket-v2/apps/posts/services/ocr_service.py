import easyocr
import cv2
import numpy as np
import matplotlib.pyplot as plt


reader = easyocr.Reader(['ko', 'en'])

def extract_words(image):
    image_bytes = image.read()
    #이미지를 넘파이 배열로 변환
    nparr = np.frombuffer(image_bytes,np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    #이미지 확대
    img = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

    #그레이 스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #노이즈 제거
    denoised = cv2.fastNlMeansDenoising(gray, h=3)

    #적응형 이진화
    # progressed_img = cv2.adaptiveThreshold(
    #     denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    #     )

    results = reader.readtext(denoised,detail=0, paragraph=True)
    return " ".join(results)

def visualize_ocr_steps(image_file):
    # 1. 파일 객체(mock_file)를 넘파이 배열로 변환하여 읽기
    file_bytes = np.frombuffer(image_file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if img is None:
        print("이미지를 불러올 수 없습니다. 경로 혹은 파일 객체를 확인하세요.")
        return

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 2. 전처리 단계들
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.fastNlMeansDenoising(gray, h=10)
    _, binary = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 3. 시각화
    titles = ['Original', 'Grayscale', 'Denoised', 'Binary']
    images = [img_rgb, gray, denoised, binary]

    plt.figure(figsize=(15, 5))
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(images[i], cmap='gray' if i > 0 else None)
        plt.title(titles[i])
        plt.axis('off') # 눈금 제거
    
    plt.tight_layout()
    plt.show()