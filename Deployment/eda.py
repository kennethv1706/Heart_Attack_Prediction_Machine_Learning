import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')
#Memanggil data csv 
    df= pd.read_csv('heart.csv')

#menampilakn 5 data teratas
    st.table(df.head(5))


#menampilakn piechart menampilkan persentase orang yang lebih besar dan lebih kecil terkena serangan jantung
    st.title('Distribusi Serangan Jantung')
    ha_freq = df['output'].value_counts()

    fig_1, ax = plt.subplots()
    ax.pie(ha_freq, labels=ha_freq.index, autopct='%1.1f%%', startangle=90)
    ax.set_title('Distribusi Serangan Jantung')
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Tidak Serangan Jantung', 'Terkena Serangan Jantung'])
    st.pyplot(fig_1)

#menampilkan penjelasan 
    with st.expander('Explanation'):
        st.caption('Hasil : Bisa dilihat bahwa yang terkena serangan jantung pada setiap pasien lebih kecil daripada yang tidak terkena serangan jantung. Kita bisa memberikan imbauan sederhana pada setiap pasien yang berobat untuk menjaga pola kesehatan pada pasien yang memiliki agar tidak terkena serangan jantung')

#Menampilkan histogram menampilkan persebaran umur pasien
    st.title("Persebaram Umur Pasien")
    fig_2= plt.figure(figsize=(6, 6))
    plt.hist(df['age'])
    plt.xlabel('Age')
    plt.ylabel('Jumlah')
    plt.title('Persebaram Umur Pasien')
    plt.tight_layout()
    plt.show()
    st.pyplot(fig_2)

#menapilkan penjelasan
    with st.expander('Explanation'):
        st.caption('Hasil : Rata-Rata Umur pasien lebih dari 40 tahun sampai 65 tahun dan pasien terbanyak ada diumur 55-60 tahun sehingga pasien pada umur tersebut. Umur yang semakin tua akan lebih rentan terkena serangan jantung walau tidak menutup kemungkinan yang lebih muda bisa terkena serangan jantung juga')

 # Membuat barplot berdasarkan tipe nyeri didada
    st.title("Tipe Nyeri Dada setelah olahraga")
    fig_3, ax  = plt.subplots(figsize=(8, 6))
    sns.countplot(x='cp', hue='exng', data=df)
    plt.title('Tipe Nyeri Dada setelah olahraga')
    plt.xlabel('Tipe Nyeri Dada')
    plt.ylabel('Count')
    st.pyplot(fig_3)

#menampilkan penjelasan
    with st.expander('Explanation'):
        st.caption('Hasil : Orang yang memiliki angina tipikal(nyeri dada yang berat) maka akan memiliki nyeri dada ketika berolahraga. Semakin rendah tingkat nyeri dada maka munculnya nyeri dada ketika berolahraga semakin sedikit')
        st.caption('Saran : Untuk pasien yang memiliki angina tipikal disarankan tidak melakukan aktifitas olahraga yang berat mungkin bisa disarankan dengan olahraga jalan kaki saja untuk mengurangi ,unculnya nyeri dada saat berolahraga')

#Menampilkan historyplot dari jumlah penyakit di pembuluh darah berdasarkan gula darah
    st.title('Jumlah of penyakit di pembuluh darah berdasarkan gula darah')
    fig_4, ax  = plt.subplots(figsize=(8, 6))
    sns.histplot(data=df, x='caa', hue='fbs', multiple="stack", stat="count")
    plt.xlabel('Jumlah penyakit di pembuluh darah')
    plt.ylabel('Count')
    plt.xticks(range(5))
    st.pyplot(fig_4)

#menampilkan penjelasan
    with st.expander("Explanation"):
        st.caption('Hasil : Kita bisa melihat bahwa semakin besar / semakin banyak penyakit dalam pembuluh darah maka presentasi pasien terkena gula darah semakin besar . Jika dilihat dari yang index 0 jumlah penyakit pembuluh darah yang sedikit maka prentasi pasien yang terkena gula darah semakin rendah begitu juga sebaliknya')
        st.caption('Saran : Orang yang memiliki penyakit di pembuluh darah yang banyak lebih baik disarankan untuk diet gula karena kemungkinan besar pasien terkena diabetes yang bisa membuat orang terkena penyakit jantung')

#menampilkan histroy plot dari detak jantung berdasarkan gender
    st.title('Detak Jantung Berdasarkan Gender')
    fig_5, ax = plt.subplots(figsize=(18, 8))
    sns.histplot(x='thalachh', hue='sex', data=df, palette=['#5C1835', '#FAE1EC'], multiple="stack", stat="count")
    plt.title('Maximum Heart Rates with Sex Distribution')
    plt.xlabel('Maximum Heart Rates')
    plt.ylabel('Number of Patients')
    st.pyplot(fig_5)

#menampilkan penjelasan
    with st.expander("Explanation"):
        st.caption('Notes : 0=Pria , 1= Wanita.') 
        st.caption('Hasil : Bisa dilihat bahwa pria memiliki detak jantuk yang tinggi dibandingkan wanita , walaupun ada wanita yang memiliki detak jantung sampai 200 itu itu dikarenakan pria lebih suka beraktivitas berat dibandingkan dengan wanita sehingga detak jantung pria berdetak lebih cepat dibandingkan dengan wanita')
        st.caption('Saran : Untuk pria bisa dipertahankan dengan aktivitas fisik yang sesuai dengan kesahatan fisik dan untuk wanita bisa ditingkatkan untuk aktivitas fisiknya sesuai dengan kondisi fisik untuk meningkatkan kesahatan jantung')

#menampilkan scatterplot dari kolestrol dan gula darah
    st.title('Kolestrol vs Tekanan Darah')
    col_sc = df.groupby('chol')['trtbps'].mean()
    fig_6, ax = plt.subplots(figsize=(18, 8))
    plt.scatter(col_sc.index, col_sc.values, alpha=0.5)
    plt.xlabel('Kolestrol')
    plt.ylabel('Tekanan Darah')
    plt.title('Kolestrol vs Tekanan Darah')
    st.pyplot(fig_6)

#menampilkan penjelasan
    with st.expander("Explanation"):
        st.caption('Hasil :Dilihat bahwa orang yang memiliki kolestrol yang semakin tinggi maka tekanan darahnya akan semakin tinggi sehingga disarankan bagi orang yang memiliki kolestrol yang tinggi sudah harus menjaga pola makan untuk menurunkan tekanan darah dalam istirahat')
        st.caption('Saran : pasien dengan kadar kolestrol dan tekanan darah yang tinggi bisa mengurangi konsumsi garam , kafein , dan alkohol. Pasien juga bisa meminum obat kolstrol dan obat darah tinggi bila memiliki kadar kolestrol dan tekanan darah yang tinggi')

#menampilakn countplot dari serangan jantung berdasarkan gender
    st.title('Serangan Jantung Berdasarkan gender')
    fig_7, ax = plt.subplots(figsize=(18, 8))
    sns.countplot(x='output', hue='sex', data=df)
    plt.xlabel('Serangan jantung')
    plt.ylabel('Count')
    st.pyplot(fig_7)

#menampilkan penjelasan
    with st.expander("Explanation"):
        st.caption('Serangan jantung : 0 = tidak serangan jantung , 1 = serangan jantung. Sex : 0 = pria , 1 = perempuan')
        st.caption('Hasil : Bisa dilihat wanita lebih banyak terkena serangan jantung dibandingkan pria , akan tetapi jika dilihat secara keseluruhan pria memiliki potensi terkena serangan jantung dibandingkan dengan wanita . Karena jumlah pria yang tidak terkena jantung berbanding cukup jauh lebih sedikit dibandingkan dengan yang terkena serangan jantung . Sehingga presentase pria yang terkena serangan jantung lebih besar daripada yang tidak terkena serangan jantung')
        st.caption('Saran : Untuk Pria lebih menjaga pola makan dan pola hidup karena kemungkinan terkena serangan jantung lebih besar , tetapi perempuan harus menjaga pola hidup dan menjaga pola makan juga karena jumlah yang terkena serangan jantung lebih besar dari pria')

    
