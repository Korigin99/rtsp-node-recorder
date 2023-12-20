import cv2
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.VideoClip import ImageClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
import numpy as np

# RTSP 주소
rtsp_url = "rtsp://admin:1234@121.152.128.114:4020/video2"

# 사용자가 원하는 자막
subtitle_text = "Your custom subtitle text here"

def add_subtitle(frame, text):
    font = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10, 50)
    fontScale = 1
    fontColor = (0, 0, 0)
    lineType = 2

    cv2.putText(frame, text,
                bottomLeftCornerOfText,
                font,
                fontScale,
                fontColor,
                lineType)

    return frame

# RTSP 비디오 스트림 열기
cap = cv2.VideoCapture(rtsp_url)

# 비디오 속성 가져오기
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# 비디오 출력 파일 설정
output_file = "output_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# 비디오 프레임 처리 및 저장
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # 프레임 처리
    processed_frame = add_subtitle(frame, subtitle_text)

    # 프레임 저장
    out.write(processed_frame)

    # 화면에 표시
    # cv2.imshow("CCTV with Subtitle", processed_frame)

    # 종료 조건
    # if cv2.waitKey(1) & 0xFF == ord('q'):
        # break

# 리소스 해제
cap.release()
out.release()
cv2.destroyAllWindows()