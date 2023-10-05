import streamlit as st
import eda
import models


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Kenneth Vincentius')
    st.write('Batch     : HCK-007')
    st.write('Tujuan Milestone    :Untuk memprediksi apakah pasien ada potensi terkena serangan jantung atau tidak dengan melihat data kesehatan pasien dengan model yang terbaik')
    st.write('')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('Saya adalah seorang data siencetist yang diberi project dari Rumah Sakit Damai Sejahtera untuk menganalisa pasien pasien apakah memiliki potensi untuk terkena serangan jantung atau tidak dengan melihat detail kesehatan dari masing-masing pasien.')

    with st.expander("Problem Statement"):
            st.caption('Problem Statement : Menurunkan angka presentase orang yang terkena serangan jantung sebanyak 3% dalam waktu 6 bulan dengan memprediksi agar bisa dicegah sebelum terkena serangan jantung berdasarkan data kesehatan pasien dengan meminimalisir recall ( false negative) pasien sakit jantung tetapi diprediksi tidak sakit jantung')

    with st.expander("Kesimpulan"):
        st.caption('Problem stament bisa terpenuhi karena recall score untuk meminimalisir false negative bisa dilakukan sebesar 96%')
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    models .run()