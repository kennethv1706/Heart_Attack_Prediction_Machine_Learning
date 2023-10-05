import streamlit as st
import pandas as pd
import pickle
import ast
from PIL import Image
import webbrowser

def run():
# Load All Files

    with open('full_process.pkl', 'rb') as file:
        full_process = pickle.load(file)


    oldpeak = st.number_input(label='penyumbatan pembuluh darah arteri koroner',min_value=0.0,max_value=6.2)
    chol = st.number_input(label='indikasi kolestrol',min_value=126,max_value=564)
    thall = st.selectbox(label='Thallium Stress Test',options=[0, 1, 2, 3])
    st.caption('Nilai 0: Tidak Ada (Normal) ,Nilai 1: Cacat Tetap, Nilai 2: Cacat Reversibel, Nilai 3: Thalassemia')
    cp = st.selectbox(label='indikasi kolestrol',options=[0, 1, 2, 3])
    st.caption('1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic')
    exng = st.selectbox(label='nyeri dada saat olahraga',options=[0, 1])
    st.caption(' 0 = tidak, 1= iya')
    sex = st.selectbox(label='gender pasien',options=[0, 1])
    st.caption('0 : male, 1 : female')
    caa =st.selectbox(label='jumlah penyakit berdasarkan pembuluh darah yang menuju jantung',options=[0, 1, 2, 3,4])
    slp =st.selectbox(label='kemiringan detak jantung saat olahraga',options=[0, 1, 2])
    st.caption('Nilai 0: Kemiringan, Nilai 1: Datar, Nilai 2: Diagnosis menanjak')

    data_inf = pd.DataFrame({
         'oldpeak' : oldpeak,
        'chol' : chol,
        'thall' : thall ,
        'cp' : cp,
        'exng' : exng ,
        'sex' : sex,
        'caa' : caa,
        'slp' : slp
        }, index =[0])

    st.table(data_inf)


    if st.button(label='predict'):
    
        # Melakukan prediksi data dummy
        y_pred_inf = full_process.predict(data_inf)

        st.write(y_pred_inf[0])

        if y_pred_inf[0] == 0:
            st.write('Pasien tidak terkena jantung')
            st.markdown("[Cara Cegah Serangan Jantung](https://www.siloamhospitals.com/informasi-siloam/artikel/cara-cegah-serangan-jantung-di-usia-muda)")

        else:
            st.write('Pasien kemungkinan terkena jantung')
            st.markdown("[Cara Hidup Sehat Sehabis Terkena Serangan Jantung](https://lifestyle.kompas.com/read/2021/11/09/101744620/7-pola-hidup-sehat-setelah-mengalami-serangan-jantung?page=all)")

