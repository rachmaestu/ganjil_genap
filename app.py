import streamlit as st

st.title(':blue[Aplikasi Bilangan Genap / Ganjil]')
st.write('Aplikasi ini digunakan untuk menentukan bilangan genap atau ganjil')

bil1 = st.number_input("Masukkan bilangan pertama:")
st.write("Bilangan pertama adalah ", bil1)

if bil1%2==0:
  st.write('Bilangan pertama termasuk bilangan genap')
else:
  st.write('Bilangan pertama termasuk bilangan ganjil')

bil2 = st.number_input("Masukkan bilangan kedua:")
st.write("Bilangan kedua adalah ", bil2)

if bil2%2==0:
  st.write('Bilangan kedua termasuk bilangan genap')
else:
  st.write('Bilangan kedua termasuk bilangan ganjil')

bil=bil1*bil2
st.write('Hasil perkalian kedua bilangan di atas adalah',bil)

if bil%2==0:
  st.write('Bilangan hasil perkalian termasuk bilangan genap')
else:
  st.write('Bilangan hasil perkalian termasuk bilangan ganjil')