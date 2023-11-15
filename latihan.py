# Membuat list dengan 5 elemen
my_list = [1, 2, 3, 4, 5]

#AKSES LIST
# Mengakses dan menampilkan elemen ke-3
print("Elemen ke-3:", my_list[2])

# Mengambil nilai elemen ke-2 sampai elemen ke-4
subset_list = my_list[1:4]
print("Nilai elemen ke-2 sampai elemen ke-4:", subset_list)

# Mengambil elemen terakhir
last_element = my_list[-1]
print("Elemen terakhir:", last_element)

#UBAH ELEMENT LIST
#ubah elemen ke 4 dengan nilai lainnya
my_list[3] = 60
print("Setelah mengubah elemen ke-4:", my_list)

#ubah elemen ke 4 sampai dengan elemen terakhir
my_list[3:] = [60, 70]
print("Setelah mengubah nilai elemen ke-4 sampai elemen terakhir:", my_list)

#TAMBAH ELEMENT LIST
# Buat list pertama (A)
A = [1, 2, 3, 4, 5]
# Ambil 2 bagian dari list pertama (A) dan jadikan list kedua (B)
B = A[:2]
print("List B:", B)

# Tambahkan list B dengan nilai string
B.append("Hello")
print("List B:" , B)

# Tambahkan list B dengan 3 nilai
B.extend([3, 4, 5])
print("List B:", B)

# Gabungkan list B dengan list A
C = B + A
print("List C (gabungan A dan B):", C)
