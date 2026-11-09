# Tugas nomor 1.a, 1.b Tuple
mahasiswa = ("Gemuruh Gampang Anugrah","2605060068","Teknologi Informasi")
print (mahasiswa[1])
print (mahasiswa[2])

# 1.c
#mahasiswa[2] = "Teknologi Informasi"
# Tugas nomor 1.d
nilai_angka = {10,4,3,2,4,10,7,5}
print (nilai_angka)

# Tugas nomor 2.a 
data_mahasiswa = {
    "nim": 240102,
    "nama": "Budi Santoso",
    "prodi": "Teknologi Informasi"
}
print(data_mahasiswa["nama"])

# Tugas nomor 2b
data_mahasiswa.update({"prodi":"Sastra Mesin" })
data_mahasiswa.update({"angkatan":2026})
print(data_mahasiswa)

# Tugas nomor 2c
del data_mahasiswa["nim"]
print(data_mahasiswa)

# Tugas nomor 3 Perulangan dictionary
keranjang = {
    "apel": 5000,
    "pisang":3000,
    "jeruk":7000,
    "anggur":15000 
}
total_belanja = 0
# Tugas nomor 3b
for buah, harga in keranjang.items():
    print(f"Harga {buah}: Rp {harga}")
    total_belanja += harga
print("-" * 25)
# Tugas nomor 3c
print(f"Total belanja: Rp {total_belanja}")
