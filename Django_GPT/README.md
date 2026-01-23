# 나만의 AI 사이트 (Django)

---
## 사용 모델 (3개 이상)

<!--
### 1. "nlptown/bert-base-multilingual-uncased-sentiment"
-**태스크**: analyze_sentiment_AI(감정 분석)
-**입력 예시** im so happy ! what a wonderful day!
-**출력 예시** ⭐ 예측 평점: 5 stars (확신도: 0.91)
- 실행 화면 예시:
-->

<!--
### 2. "google/pegasus-xsum"
-**태스크**: summarizationAI (요약)
-**입력 예시**
"The photoelectric effect is the emission of electrons when electromagnetic radiation, such as light, hits a material. Photons with energy higher than the work function of the material can knock electrons loose. This phenomenon was crucial in the development of modern physics as it provided evidence for the particle-like behavior of light, leading to Albert Einstein's Nobel Prize."
-**출력 예시**
Researchers at the University of California, Berkeley, say they have discovered a new type of photoelectric particle.
- 실행 화면 예시:
-->

<!--
### 3. "HuggingFaceTB/SmolLM2-1.7B-Instruct"
-**태스크**: text-generation AI (문장생성)
-**입력 예시**
"A block of mass $m$ slides down a frictionless incline of height $h$. Calculate its final velocity at the bottom using the principle of conservation of energy."
-**출력 예시**
To solve this, we can use the principle of conservation of energy. The total energy of the block before it slides down the incline is the sum of its kinetic energy, potential energy, and the energy due to its own mass. Initial energy = Potential energy + Kinetic energy + Energy due to mass Let's denote the kinetic energy as K_initial = (1/2)mv^2, the potential energy by U_initial = mgh, and the energy due
- 실행 화면 예시:
-->

---
## 로그인 제한(Access Control)

- 비로그인 사용자는**1개 탭만 사용 가능**
- 제한 탭 접근 시**“로그인 후 이용해주세요” alert 후 로그인 페이지로 이동**
- 로그인 성공 시**원래 페이지로 복귀(next)**

---
## 구현 체크리스트

- [o ] 탭 3개 이상 + 각 탭 별 URL 분리
- [o ] 각 탭: 입력 → 실행 → 결과 출력
- [x ] 에러 처리: 모델 호출 실패 시 사용자에게 메시지 표시
- [ x] 로딩 표시(최소한 “처리 중…” 텍스트라도)
- [ x] 요청 히스토리 5개
- [ o]`.env` 사용 (토큰/API Key 노출 금지)
- [ 0]`README.md`에 모델 정보/사용 예시/실행 방법 작성 후 GitHub push

### 로그인 제한 체크
- [o ] 비로그인 사용자는 1개 탭만 접근 가능
- [ o] 제한 탭 접근 시 alert 후 로그인 페이지로 redirect
- [ o] 로그인 성공 시 원래 페이지로 복귀(next)