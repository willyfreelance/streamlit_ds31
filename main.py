import streamlit as st

st.set_page_config(page_title="Portfolio",
                   layout="wide", page_icon=":rocket:")

st.title("Portfolio Saya")
st.header("Data Scientist & Developer")

st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman",
                        ["Tentang Saya", "Proyek", "Machine Learning", "Kontak"])


if page == 'Tentang Saya':
    import tentang
    tentang.tampilkan_tentang_saya()
elif page == 'Kontak':
    import kontak
    kontak.tampilkan_kontak()
elif page == 'Proyek':
    import proyek
    proyek.tampilkan()
else:
    import machine_learning
    machine_learning.prediksi()