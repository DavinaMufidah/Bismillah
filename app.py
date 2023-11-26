import streamlit as st
from sqlalchemy import text

list_tipe_kamar = ['', 'Standard Room', 'Superior Room', 'Deluxe Room', 'Junior Suite Room', 'Suite Room']
list_gender = ['', 'Laki-laki', 'Perempuan']
list_needs = ['', 'Paket Sarapan', 'Private Swimming Pool', 'Golf Access', 'Gym Access', 'Tennis Access']

conn = st.connection("postgresql", type="sql",
                     url="postgresql://davina.mufidah97.dm:Bdq9QfNnMH8e@ep-quiet-sound-44554664.us-east-2.aws.neon.tech/web")
with conn.session as session:
    query = text('CREATE TABLE IF NOT EXISTS hotel (id serial, nama text, gender text, tanggal_pemesanan date, '
                 'tanggal_menginap date, tipe_kamar text, nomor_kamar text, handphone text, needs text);')
    session.execute(query)

st.header('HOTEL DATA MANAGEMENT SYSTEM')
page = st.sidebar.selectbox("Pilih Menu", ["View Data", "Edit Data"])

if page == "View Data":
    data = conn.query('SELECT * FROM hotel ORDER By id;', ttl="0").set_index('id')
    st.dataframe(data)

if page == "Edit Data":
    if st.button('Tambah Data'):
        with conn.session as session:
            query = text('INSERT INTO hotel (nama, gender, tanggal_pemesanan, tanggal_menginap, tipe_kamar, \
                          nomor_kamar, handphone, needs) VALUES (:1, :2, :3, :4, :5, :6, :7, :8);')
            session.execute(query, {'1': '', '2': '', '3': None, '4': None, '5': '', '6': '', '7':'', '8': '[]'})
            session.commit()

    data = conn.query('SELECT * FROM hotel ORDER By id;', ttl="0")
    for _, result in data.iterrows():
        id = result['id']
        nama_lama = result["nama"]
        gender_lama = result["gender"]
        tanggal_pemesanan_lama = result["tanggal_pemesanan"]
        tanggal_menginap_lama = result["tanggal_menginap"]
        tipe_kamar_lama = result["tipe_kamar"]
        nomor_kamar_lama = result["nomor_kamar"]
        handphone_lama = result["handphone"]
        needs_lama = result["needs"]

        with st.expander(f'a.n. {nama_lama}'):
            with st.form(f'data-{id}'):
                nama_baru = st.text_input("nama", nama_lama)
                gender_baru = st.selectbox("gender", list_gender, list_gender.index(gender_lama) if gender_lama in list_gender else 0)
                tanggal_pemesanan_baru = st.date_input("tanggal_pemesanan", tanggal_pemesanan_lama)
                tanggal_menginap_baru = st.date_input("tanggal_menginap", tanggal_menginap_lama)
                tipe_kamar_baru = st.selectbox("tipe_kamar", list_tipe_kamar, list_tipe_kamar.index(tipe_kamar_lama) if tipe_kamar_lama in list_tipe_kamar else 0)
                nomor_kamar_baru = st.text_input("nomor_kamar", nomor_kamar_lama)
                handphone_baru = st.text_input("handphone", handphone_lama)
                needs_baru = needs_baru = st.multiselect("needs", list_needs, default=list(filter(lambda x: x in list_needs, eval(needs_lama))))
                
                col1, col2 = st.columns([1, 6])

                with col1:
                    if st.form_submit_button('UPDATE'):
                        with conn.session as session:
                            query = text('UPDATE hotel'
                            'SET nama=:nama, gender=:gender, tanggal_pemesanan=:tanggal_pemesanan, '
                            'tanggal_menginap=:tanggal_menginap, tipe_kamar=:tipe_kamar, nomor_kamar=:nomor_kamar, ' 
                            'handphone=:handphone, needs=:needs '
                            'WHERE id=:id;')
                            session.execute(query, {'1': nama_baru, '2': gender_baru, '3': tanggal_pemesanan_baru,
                            '4': tanggal_menginap_baru,
                            '5': tipe_kamar_baru, '6': nomor_kamar_baru,
                            '7': handphone_baru, '8': str(needs_baru), '9': id})
                            session.commit()
                            st.experimental_rerun()

                with col2:
                    if st.form_submit_button('DELETE'):
                        query = text(f'DELETE FROM hotel WHERE id=:id;')
                        session.execute(query, {'1': id})
                        session.commit()
                        st.experimental_rerun()
