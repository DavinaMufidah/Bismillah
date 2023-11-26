drop table if exists hotel;
create table hotel (
    id serial,
    nama text,
    gender text,
    tanggal_pemesanan date,
    tanggal_menginap date,
    tipe_kamar text,
    nomor_kamar text,
    handphone text,
    needs text
);

insert into hotel (nama, gender, tanggal_pemesanan, tanggal_menginap, tipe_kamar, nomor_kamar, handphone, needs) 
values
    ('Andhika Putra', 'Laki-laki', '2023-02-05', '2023-02-07', 'Standard Room', '102', '62898', '["Paket Sarapan", "Gym Access"]'),
    ('Sulistiawati Hartanto', 'Perempuan', '2023-10-09', '2023-10-11', 'Superior Room', '108', '62788', '["Paket Sarapan", "Private Swimming Pool"]'),
    ('Sutrisno Mengkubuono', 'Laki-laki', '2023-01-08', '2023-01-12', 'Deluxe Room', '115', '62567', '["Tennis Access", "Private Swimming Pool"]'),
    ('Sajidah Nur', 'Perempuan', '2023-11-01', '2023-11-01', 'Junior Suite Room', '377', '62889', '["Private Swimming Pool", "Gym Access", "Paket Sarapan"]'),
    ('Afilian Nugroho', 'Laki-laki', '2023-09-05', '2023-09-06', 'Superior Room', '309', '62645', '["Tennis Access", "Golf Access"]'),
    ('Rahmad Cendekiawan', 'Laki-laki', '2023-05-05', '2023-05-07', 'Deluxe Room', '129', '62223', '["Paket Sarapan", "Gym Access"]'),
    ('Aliansyah Firmantio', 'Laki-laki', '2023-02-02', '2023-02-02', 'Suite Room', '206', '62458', '["Gym Access", "Golf Access", "Paket Sarapan"]'),
    ('Aisyah Putri', 'Perempuan', '2023-12-12', '2023-12-14', 'Junior Suite Room', '222', '62321', '["Tennis Access", "Paket Sarapan"]'),
    ('Putri Indaswari', 'Perempuan', '2023-10-10', '2023-10-12', 'Deluxe Room', '324', '62577', '["Paket Sarapan", "Gym Access", "Tennis Access"]'),
    ('Azizah Nurani', 'Perempuan', '2023-08-29', '2023-08-30', 'Superior Room', '411', '62790', '["Paket Sarapan", "Private Swimming Pool", "Gym Access"]')
    ;
