import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from io import BytesIO


def load(text, x,y):
    # 이미지 업로드
    image = Image.open('resource/empty_image.png')

    # 사용자가 입력한 텍스트
  
    drawn_image = draw_with_load(image, text, x, y)
    st.image(drawn_image, use_column_width=True)
    

    download_image_btn(drawn_image)


def main():
    # 초기 텍스트 위치 설정
  st.set_page_config(layout="wide")
  col1, col2 = st.columns([0.5,0.3])

  x = 30.0
  y = 150.0
  text = "    아저씨,\n우체국이 어딘지\n    아세요?"

  with col2:
    text = st.text_area("이미지에 그릴 텍스트를 입력하세요.", text, key="text_area")     
    # 텍스트 X, Y 좌표 슬라이더 생성
    x = st.slider('텍스트 X 좌표', 0.0, 100.0, x, key="x_slider")
    y = st.slider('텍스트 Y 좌표', 100.0, 200.0, y, key="y_slider")
  
  with col1:
  # 텍스트 X, Y 좌표가 변경될 때마다 load() 함수 호출하여 이미지 업데이트
    if st.session_state.x_slider is not None or st.session_state.y_slider is not None or st.session_state.text_area is not None:
      load(text, x, y)
  
        

def draw_with_load(image, text, x, y):
    drawn_image = draw_text_on_image(image, text, x, y)
    return drawn_image

def download_image_btn(image):
    buf = BytesIO()
    image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
            label="다운로드",
            data=byte_im,
            file_name="ok_meme.png",
            mime="image/png"
        )

def draw_text_on_image(image, text, x, y):
    img_with_text = image.copy()
    draw = ImageDraw.Draw(img_with_text)

    # 폰트 설정
    font = ImageFont.truetype("resource/NanumGothic-ExtraBold.ttf", size=14)

    # 텍스트 위치 설정
    text_x = x
    text_y = y

    # 텍스트 그리기
    text_color = (88, 93, 114)
    draw.text((text_x, text_y), text, fill=text_color, font=font)

    return img_with_text

if __name__ == "__main__":
    main()