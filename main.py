import streamlit as st
import base64

# Fungsi untuk menyisipkan file CSS/HTML
def local_css(background_image):
    with open(background_image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
        }}
        h1 {{
            color: #fff;
            font-size: 50px;
            text-align: center;
            text-shadow: 3px 3px 15px rgba(0,0,0,0.7);
            animation: float 3s infinite;
            margin-top: 100px;
        }}
        @keyframes float {{
            0% {{ transform: translateY(0px); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0px); }}
        }}
        .slide-container {{
            text-align: center;
            margin-top: 100px;
        }}
        .slide {{
            font-size: 24px;
            color: #fff;
            text-align: center;
            padding: 20px;
            background: rgba(0, 0, 0, 0.6);
            border-radius: 15px;
            width: 70%;
            margin: auto;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            animation: fadeIn 1s;
        }}
        @keyframes fadeIn {{
            from {{opacity: 0;}}
            to {{opacity: 1;}}
        }}

        @keyframes wave {{
            0% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-10px); }}
            100% {{ transform: translateY(0); }}
        }}

        .button-container {{
            text-align: center;
            margin-top: 20px;
        }}
        .button {{
            background-color: #ff4081;
            color: white;
            padding: 15px 25px;
            font-size: 18px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            transition: 0.3s;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        .button:hover {{
            background-color: #e91e63;
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
        }}

        .button:active {{
            transform: translateY(0);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}

        .footer {{
            text-align: center;
            margin-top: 70px;
            font-size: 20px;
            color: #fff;
            animation: wave 1s infinite;
            text-shadow: 1px 1px 5px rgba(0,0,0,0.5);
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Background gambar pribadi
background_image = "./bg_main.png"
local_css(background_image)

# Judul dan nama
st.markdown("<h1>🎉 Selamat Ulang Tahun! 🎂</h1>", unsafe_allow_html=True)

nama_teman = "AYA CHAN"
st.markdown(f"<h2 style='text-align: center; color: #fff; text-shadow: 2px 2px 10px rgba(0,0,0,0.5);'><b>{nama_teman}</b>, yang ke 19 + 3</h2>", unsafe_allow_html=True)

# Slide Interaktif
slides = [
    "💖 Selamat ya Panda chan....",
    "🎁 Semoga Panjang Umur, Sehat Selalu!",
    "🌟 Lancar Rezekinya!",
    "🚀 Semoga semua impian dan harapan jadi kenyataan!",
    "💡 Bareng terus sama Ayam yaaa",
]

# Gunakan session state untuk menyimpan indeks slide
if "current_slide" not in st.session_state:
    st.session_state.current_slide = 0

def update_slide():
    st.session_state.current_slide = (st.session_state.current_slide + 1) % len(slides)

# Menampilkan slide pertama
slide_placeholder = st.empty()
slide_placeholder.markdown(f"<div class='slide'>{slides[st.session_state.current_slide]}</div>", unsafe_allow_html=True)

# Tombol untuk slide berikutnya
st.markdown("<div class='button-container'>", unsafe_allow_html=True)
st.button("GAS PENCET LAGI 🎊", on_click=update_slide)
st.markdown("</div>", unsafe_allow_html=True)

# Tampilkan pesan dari Anda di bagian bawah
st.markdown("<div class='footer'><b>💌 Dari: AYAM BAIK</b></div>", unsafe_allow_html=True)

# Efek balon
st.balloons()
st.balloons()
st.balloons()
