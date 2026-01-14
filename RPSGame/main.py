import mediapipe as mp
import cv2 as cv
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time
from visualization import draw_manual,print_RSP_result
from webcam import cv2_stream

latest_result = None

def update_result(result, output_image, timestamp_ms):
    global latest_result
    latest_result = result

base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(
    running_mode=vision.RunningMode.LIVE_STREAM,
    base_options=base_options,
    num_hands=1,
    result_callback=update_result
)

if __name__ == "__main__":
    cap = cv.VideoCapture(0)
    with vision.HandLandmarker.create_from_options(options) as landmarker:
        while cap.isOpened():
            ret,frame = cap.read()
            if not ret:
                print("can't receive frame")
                break

            frame = cv.flip(frame,1) # 거울모드

            #rgb랑 mp전처리 프레임 생성
            rgb_frame = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
            mp_frame = mp.Image(image_format=mp.ImageFormat.SRGB,data=rgb_frame)

            #현재 시간을 ms단위 넘김
            timestamp = int(time.time()*1000)
            landmarker.detect_async(mp_frame,timestamp)

            if latest_result is not None:
                frame,rps_result = draw_manual(frame,latest_result)
                print_RSP_result(frame,rps_result)

            cv.imshow('frame',frame)
            if cv.waitKey(1) == ord('q'):
                break
    cap.release()
    cv.destroyAllWindows()