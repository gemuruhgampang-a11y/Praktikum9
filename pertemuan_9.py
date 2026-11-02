# Program 9.1
# list
x = [1,2,3]
print(x)

# balternatif membuat list (int)
# range(start, stop, step)
data_range = range(0,10,2)
print(data_range)
data_list = list(data_range)
print(data_list)

# Kumpulan int
data_angka = [3,5,1,8]
print(data_angka)

# Kumpulan str
data_str = ["ucup","adit","siti"]
print(data_str)

# Kumpulan bool
data_bool = [True, False, True, False]
print(data_bool)

# Kumpulan campuran
data_campuran = [3,"aci",True,8,False,"opelasurus"]
print(data_campuran)

# membuat listr dgn for dgn if
list_for_if = [i for i in range(0,10) if i != 5]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i == 5]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i % 2 == 0]
print(list_for_if)

list_for_if = [i for i in range(0,10) if i % 2 != 0]
print(list_for_if)

list_for = [i **2 for i in range(0,10)]
print(list_for)

# Program 9.2 Manupulasi List
data = ["ucup","adit","siti"] 
#          0      1      2
#         -3     -2     -1
# Mengambil data list
print(data[0])
# Mengambil data list dari belakang
print(data[-1])

# Menambah data list sesuai index
data.insert(1, "Asep")
print(data)

# Menambah data list di akhir
data.append("Opung")
print(data)

# Menambah data list dengan List lain
baru = ["Opel", "Ai", "Ada"]
data.extend(baru)
print(data)

# Merubah data list sesuai index
data[2] = "jarwo"
print(data)

# Menghapus data list sesuai index
data.remove("ucup")
print(data)

# Menghapus data paling belakang list
data.pop()
print(data)

# Menghitung jumlah data list
panjang_data = len(data)
print(panjang_data)

# Program 9.3 Operasi List
angka = [0,5,1,4,6,2,8,0,1,5,8,9]
print(angka)

# count data
data_1 = angka.count(1)
data_5 = angka.count(5)
print(data_1)
print(data_5)

# mengurutkan list
angka.sort()
print(angka)

# membalikkan list
angka.reverse()
print(angka)

# Mengambil posisi data
data = ["ucup","adit","siti"]
index_ucup = data.index("ucup")
index_adit = data.index("adit")
print(index_ucup)
print(index_adit)

# 9.4 Nested List
data_0 = [1,2]
data_1 = [3,4]
data_list = [1,2,3,4]
print(data_list)
list = [data_0, data_1]
print(list)

# Contoh Penggunaan Nested List
peserta_0 = ["Jamil", 30, "Laki-laki"]
peserta_1 = ["Masiran", 29, "Laki-laki"]
peserta_2 = ["Supri", 45, "Laki-laki"]
list_peserta = [peserta_0, peserta_1, peserta_2]
print(list_peserta)
# for di nested list
for peserta in list_peserta:
    print(f"Nama Peserta: {peserta[0]}")
    print(f"Umur        : {peserta[1]}")
    print(f"gender      : {peserta[2]}")
    print()