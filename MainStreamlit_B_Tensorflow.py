import streamlit as st
import pickle
import os

from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu("Tugas UTS 2024/2025",
                           ['Klasifikasi','Regresi'],default_index=0)
    
if selected == 'Klasifikasi':
    model_path = r'BestModel_CLF_GBT_Tensorflow.pkl'

    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    st.title('Klasifikasi')
    st.write('Masukkan Input-input berikut ini')
    luas = st.slider('Luas', 0, 99999)
    jumlah_ruangan = st.slider('Jumlah Ruangan', 0, 100)
    halaman = st.selectbox('Halaman', ['Ada', 'Tidak Ada'])
    kolam = st.selectbox('Kolam', ['Ada', 'Tidak Ada'])
    lantai = st.slider('Lantai', 0, 100)
    kode_lokasi = st.number_input('Kode Lokasi', 0, 99953)
    ekslusifitas_kawasan = st.number_input('Ekslusifitas Kawasan', 0, 10)
    jumlah_pemilik_sebelumnya = st.number_input('Jumlah Pemilik Sebelumnya', 0, 10)
    tahun_pembangunan = st.slider('Tahun Pembangunan', 1990, 2021)
    baru = st.selectbox('Apakah Baru', ['Baru', 'Tidak Baru'])
    punyaStormProctector = st.selectbox('Punya Storm Protector', ['Punya', 'Tidak Punya'])
    luas_basement = st.slider('Luas Basement', 0, 10000)
    luas_loteng = st.slider('Luas Loteng', 0, 10000)
    luas_garasi = st.slider('Luas Garasi', 0, 10000)
    gudang = st.selectbox('Gudang', ['Ada', 'Tidak Ada'])
    jumlah_kamar_tamu = st.number_input('Jumlah Kamar Tamu', 0, 10)

    if halaman == 'Ada':
        halaman_ada = 1
        halaman_tidak_ada = 0
    elif halaman == 'Tidak Ada':
        halaman_ada = 0
        halaman_tidak_ada = 1
    
    if kolam == 'Ada':
        kolam_ada = 1
        kolam_tidak_ada = 0
    elif kolam == 'Tidak Ada':
        kolam_ada = 0
        kolam_tidak_ada = 1

    if baru == 'Baru':
        baru_baru = 1
        baru_tidak_baru = 0
    elif baru == 'Tidak Baru':
        baru_baru = 0
        baru_tidak_baru = 1

    if punyaStormProctector == 'Punya':
        punya_storm_protector_punya = 1
        punya_storm_protector_tidak_punya = 0
    elif punyaStormProctector == 'Tidak Punya':
        punya_storm_protector_punya = 0
        punya_storm_protector_tidak_punya = 1
    
    if gudang == 'Ada':
        gudang_ada = 1
        gudang_tidak_ada = 0
    elif gudang == 'Tidak Ada':
        gudang_ada = 0
        gudang_tidak_ada = 1
    
    input_data = [[luas, jumlah_ruangan, halaman_ada, halaman_tidak_ada, kolam_ada, kolam_tidak_ada, lantai, kode_lokasi, ekslusifitas_kawasan, jumlah_pemilik_sebelumnya, tahun_pembangunan, baru_baru, baru_tidak_baru, punya_storm_protector_punya, punya_storm_protector_tidak_punya, luas_basement, luas_loteng, luas_garasi, gudang_ada, gudang_tidak_ada, jumlah_kamar_tamu]]

    

    if st.button('Prediksi'):
        model = model.predict(input_data)
        st.write('Kategori yang diprediksi adalah', model)

elif selected == 'Regresi':

    model_path = r'BestModel_REG_Lasso_Tensorflow.pkl'

    with open(model_path, 'rb') as file:
        model = pickle.load(file)

    st.title('Regresi')
    st.write('Masukkan Input-input berikut ini')
    luas = st.slider('Luas', 0, 99999)
    jumlah_ruangan = st.slider('Jumlah Ruangan', 0, 100)
    halaman = st.selectbox('Halaman', ['Ada', 'Tidak Ada'])
    kolam = st.selectbox('Kolam', ['Ada', 'Tidak Ada'])
    lantai = st.slider('Lantai', 0, 100)
    kode_lokasi = st.number_input('Kode Lokasi', 0, 99953)
    ekslusifitas_kawasan = st.number_input('Ekslusifitas Kawasan', 0, 10)
    jumlah_pemilik_sebelumnya = st.number_input('Jumlah Pemilik Sebelumnya', 0, 10)
    tahun_pembangunan = st.slider('Tahun Pembangunan', 1990, 2021)
    baru = st.selectbox('Apakah Baru', ['Baru', 'Tidak Baru'])
    punyaStormProctector = st.selectbox('Punya Storm Protector', ['Punya', 'Tidak Punya'])
    luas_basement = st.slider('Luas Basement', 0, 10000)
    luas_loteng = st.slider('Luas Loteng', 0, 10000)
    luas_garasi = st.slider('Luas Garasi', 0, 10000)
    gudang = st.selectbox('Gudang', ['Ada', 'Tidak Ada'])
    jumlah_kamar_tamu = st.number_input('Jumlah Kamar Tamu', 0, 10)

    if halaman == 'Ada':
        halaman_ada = 1
        halaman_tidak_ada = 0
    elif halaman == 'Tidak Ada':
        halaman_ada = 0
        halaman_tidak_ada = 1
    
    if kolam == 'Ada':
        kolam_ada = 1
        kolam_tidak_ada = 0
    elif kolam == 'Tidak Ada':
        kolam_ada = 0
        kolam_tidak_ada = 1

    if baru == 'Baru':
        baru_baru = 1
        baru_tidak_baru = 0
    elif baru == 'Tidak Baru':
        baru_baru = 0
        baru_tidak_baru = 1

    if punyaStormProctector == 'Punya':
        punya_storm_protector_punya = 1
        punya_storm_protector_tidak_punya = 0
    elif punyaStormProctector == 'Tidak Punya':
        punya_storm_protector_punya = 0
        punya_storm_protector_tidak_punya = 1
    
    if gudang == 'Ada':
        gudang_ada = 1
        gudang_tidak_ada = 0
    elif gudang == 'Tidak Ada':
        gudang_ada = 0
        gudang_tidak_ada = 1
    
    input_data = [[luas, jumlah_ruangan, halaman_ada, halaman_tidak_ada, kolam_ada, kolam_tidak_ada, lantai, kode_lokasi, ekslusifitas_kawasan, jumlah_pemilik_sebelumnya, tahun_pembangunan, baru_baru, baru_tidak_baru, punya_storm_protector_punya, punya_storm_protector_tidak_punya, luas_basement, luas_loteng, luas_garasi, gudang_ada, gudang_tidak_ada, jumlah_kamar_tamu]]

    

    if st.button('Prediksi'):
        model = model.predict(input_data)
        st.write('Harga yang diprediksi adalah', model)

        

