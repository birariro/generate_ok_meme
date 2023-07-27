import streamlit as st
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


def draw(image, text, x,y):

    drawn_image = draw_text_on_image(image, text, x, y)
    st.image(drawn_image, use_column_width=True)
    show_download_btn(drawn_image)

def show_download_btn(image):
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

    font = ImageFont.truetype("resource/NanumGothic-ExtraBold.ttf", size=14)

    text_x = x
    text_y = y
    text_color = (88, 93, 114)

    draw.text((text_x, text_y), text, fill=text_color, font=font)

    return img_with_text


def main():
  st.set_page_config(layout="wide")
  left, right = st.columns([0.5,0.3])

  x = 30.0
  y = 150.0
  text = "    아저씨,\n우체국이 어딘지\n    아세요?"
  image = Image.open('resource/empty_image.png')
  

  with right:
    text = st.text_area("이미지에 그릴 텍스트를 입력하세요.", text, key="text_area")     
    x = st.slider('텍스트 X 좌표', 0.0, 100.0, x, key="x_slider")
    y = st.slider('텍스트 Y 좌표', 100.0, 200.0, y, key="y_slider")
    uploaded_file = st.file_uploader("Upload your file here...", type=['png', 'jpeg', 'jpg'],key="upload_image")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
    
  with left:
    if st.session_state.x_slider is not None or st.session_state.y_slider is not None or st.session_state.text_area is not None or st.session_state.upload_image is not None:
      draw(image, text, x, y)
  
    

if __name__ == "__main__":
    main()