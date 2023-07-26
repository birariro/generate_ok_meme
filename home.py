import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from io import BytesIO

def main():

  image = Image.open('resource/empty_image.png')
  st.image(Image.open('resource/sample_image.png'))

  x_slider = st.slider('텍스트 X 좌표', 0.0, 100.0, 30.0)
  y_slider = st.slider('텍스트 Y 좌표', 100.0, 200.0, 150.0)

  text_to_draw = st.text_area("이미지에 그릴 텍스트를 입력하세요.", "    아저씨,\n우체국이 어딘지\n    아세요?")

  if st.button("그리기"):
    # 이미지에 텍스트 그리기
    drawn_image = draw_text_on_image(image, text_to_draw, x_slider,y_slider)
    st.image(drawn_image, use_column_width=True)

    buf = BytesIO()
    drawn_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
            label="다운로드",
            data=byte_im,
            file_name="ok_meme.png",
            mime="image/png"
          )
  

def draw_text_on_image(image, text,x,y):
  img_with_text = image.copy()
  draw = ImageDraw.Draw(img_with_text)

  # 폰트 설정 (예: 폰트 파일이 있는 경로를 지정하거나 기본 시스템 폰트 사용)
  font = ImageFont.truetype("resource/NanumGothic-ExtraBold.ttf", size=14) 

  # 텍스트 위치 설정 (임의의 위치)
  text_x = x
  text_y = y

  # 텍스트 그리기
  text_color = (88, 93, 114) 
  draw.text((text_x, text_y), text, fill=text_color,font=font)

  return img_with_text

if __name__ == "__main__":
  main()