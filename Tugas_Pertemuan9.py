# 1. Diberikan List
kendaraan = ["motor","mobil","sepeda","bus"]
# a. Menambahkan data "truk" di akhir list
kendaraan.append("truk")
print(kendaraan)
# b. Sisipkan "becak" pada index ke-1
kendaraan.insert(1,"becak")
print(kendaraan)
# c. Hapus data paling belakang
kendaraan.pop()
print(kendaraan)
# d. Ubah elemen "sepeda" menjadi "skuter"
kendaraan[2] = "skuter"
print(kendaraan)
# e. Tapilkan Jumlah total data dalam satu list
panjang_data = len(kendaraan)
print(panjang_data)
print()
# 2. Diberikan List
angka = [75,80,90,75,85,100,65]
# a. Cari tahu index berapa 100 berada
index_100 = angka.index(100)
print(index_100)
# b. Hitung jumlah data 75
count_75 = angka.count(75)
print(count_75)
# c. Urutkan data dari kecil ke besar
angka.sort()
print(angka)
# balikkan data dari besar ke kecil
angka.reverse()
print(angka)
print()
# 3. Diberikan Nested List
menu_utama = ["Nasi Goreng", "Mie Ayam"]
menu_tambahan = ["Kerupuk", "Es Teh"]
# Gabungkan menu utama dan menu tambahan menjadi satu list
menu = [menu_utama, menu_tambahan]
print(menu)
print()
# 4. Diberikan Nested List
data_barang = [["Buku", 5000], ["pensil", 2000], ["Penggaris", 3000]]
# a. Tambilkan harga dari "pensil"(2000) dengan memanggil index baris dan kolomnya
print(f"Harga dari pensil: {data_barang[1][1]}")
print()
# b. Gunakan perulangan untuk membaca 1 per 1
for barang in data_barang:
    print(f"Nama: {barang[0]}")
    print(f"Harga: {barang[1]}")
    print()